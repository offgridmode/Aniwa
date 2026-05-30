import platform
import time
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Optional

import polars as pl
import typer
from rich.console import Console
from rich.table import Table

from aniwa.config_loader import get_flattened_config
from aniwa.core.profiler import profile_dataframe
from aniwa.io.readers import read_dataset
from aniwa.models.enums import ReportSection
from aniwa.models.profile import ProfileMetadata
from aniwa.reports.console import render_console_report
from aniwa.reports.excel_report import render_excel_report
from aniwa.reports.html_report import render_html_report
from aniwa.reports.json_report import render_json_report
from aniwa.reports.markdown_report import render_markdown_report
from aniwa.reports.pdf_report import render_pdf_report
from aniwa.utils.progress import ProgressTracker
from aniwa.utils.logging import configure_logger, VerbosityLevel, get_logger, log_debug, log_info, log_success, log_verbose, log_warning, log_error
from aniwa.presets import apply_preset, list_presets, get_preset


app = typer.Typer(help="Aniwa - Universal dataset profiling and intelligence.")
console = Console()

def version_callback(value: bool):
    """Display version and exit."""
    if value:
        from aniwa import __version__

        console.print(f"aniwa version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
):
    """Aniwa - Universal dataset profiling and intelligence."""
    pass

CONFIG_FILE_NAMES = (
    "aniwa.yaml",
    "aniwa.yml",
    "aniwa.toml",
    "aniwa.json",
)


class ReportFormat(str, Enum):
    console = "console"
    json = "json"
    html = "html"
    excel = "excel"
    markdown = "markdown"
    pdf = "pdf"


class ProfileMode(str, Enum):
    fast = "fast"
    deep = "deep"


def validate_sections(value: str | None) -> list[str] | None:
    if not value:
        return None

    split_sections = [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]

    if not split_sections:
        return None

    valid_options = [section.value for section in ReportSection]

    for section in split_sections:
        if section not in valid_options:
            raise typer.BadParameter(
                f"Invalid report section: {section}. "
                f"Valid options are: {', '.join(valid_options)}."
            )

    return split_sections


def resolve_sections(
    include: str | None,
    exclude: str | None,
) -> set[ReportSection]:
    include_sections = validate_sections(include)
    exclude_sections = validate_sections(exclude)

    if include_sections and exclude_sections:
        raise typer.BadParameter("Use either --include or --exclude, not both.")

    all_sections = set(ReportSection)

    if include_sections:
        return {ReportSection(section) for section in include_sections}

    if exclude_sections:
        return all_sections - {ReportSection(section) for section in exclude_sections}

    return all_sections


def discover_config_file() -> str | None:
    for filename in CONFIG_FILE_NAMES:
        path = Path.cwd() / filename

        if path.exists():
            return str(path)

    return None


def load_active_config(config_file: str | None) -> dict[str, Any]:
    if config_file:
        path = Path(config_file)

        if not path.exists():
            raise typer.BadParameter(f"Configuration file not found: {config_file}")

        try:
            return get_flattened_config(str(path))
        except ValueError as exc:
            raise typer.BadParameter(f"Configuration error: {exc}") from exc

    discovered_config = discover_config_file()

    if discovered_config is None:
        return {}

    try:
        return get_flattened_config(discovered_config)
    except ValueError as exc:
        raise typer.BadParameter(f"Configuration error: {exc}") from exc


def resolve_report_format(value: ReportFormat | str | None) -> ReportFormat:
    if value is None:
        return ReportFormat.console

    if isinstance(value, ReportFormat):
        return value

    try:
        return ReportFormat(value)
    except ValueError as exc:
        valid_options = ", ".join(item.value for item in ReportFormat)
        raise typer.BadParameter(
            f"Invalid report format: {value}. "
            f"Valid options are: {valid_options}."
        ) from exc


def resolve_profile_mode(value: ProfileMode | str | None) -> ProfileMode:
    if value is None:
        return ProfileMode.deep

    if isinstance(value, ProfileMode):
        return value

    try:
        return ProfileMode(value)
    except ValueError as exc:
        valid_options = ", ".join(item.value for item in ProfileMode)
        raise typer.BadParameter(
            f"Invalid profiling mode: {value}. "
            f"Valid options are: {valid_options}."
        ) from exc


def resolve_output_path(
    output: str | None,
    output_dir: str | None,
    report: ReportFormat,
) -> str | None:
    if output and output_dir:
        raise typer.BadParameter("Use either --output or --output-dir, not both.")

    if report == ReportFormat.console:
        return None

    if output:
        return output

    if output_dir:
        return str(Path(output_dir) / resolve_default_name(report))

    return resolve_default_name(report)


def resolve_default_name(report: ReportFormat) -> str:
    default_names = {
        ReportFormat.json: "aniwa_report.json",
        ReportFormat.html: "aniwa_report.html",
        ReportFormat.excel: "aniwa_report.xlsx",
        ReportFormat.markdown: "aniwa_report.md",
        ReportFormat.pdf: "aniwa_report.pdf",
    }

    return default_names.get(report, "aniwa_report.txt")


def ensure_output_parent(output: str | None) -> None:
    if output is None:
        return

    Path(output).parent.mkdir(parents=True, exist_ok=True)


def format_file_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"

    if size_bytes < 1024**2:
        return f"{size_bytes / 1024:.2f} KB"

    if size_bytes < 1024**3:
        return f"{size_bytes / 1024**2:.2f} MB"

    return f"{size_bytes / 1024**3:.2f} GB"


def build_command_used(
    path: str,
    report: ReportFormat,
    output: str | None,
    output_dir: str | None,
    mode: ProfileMode,
    include: str | None,
    exclude: str | None,
    template: str,
    config_file: str | None,
    verbosity: VerbosityLevel,
    preset: Optional[str] = None,
) -> str:
    command_parts = ["aniwa", path]

    if preset:
        command_parts.extend(["--preset", preset])

    if config_file:
        command_parts.extend(["--config", config_file])

    if report != ReportFormat.console:
        command_parts.extend(["--report", report.value])

    if output:
        command_parts.extend(["--output", output])

    if output_dir:
        command_parts.extend(["--output-dir", output_dir])

    if mode != ProfileMode.deep:
        command_parts.extend(["--mode", mode.value])

    if include:
        command_parts.extend(["--include", include])

    if exclude:
        command_parts.extend(["--exclude", exclude])

    if report in {ReportFormat.html, ReportFormat.pdf} and template != "default":
        command_parts.extend(["--template", template])
    
    if verbosity != VerbosityLevel.NORMAL:
        command_parts.extend(["--verbosity", verbosity.value])

    return " ".join(command_parts)


def build_profile_metadata(
    dataset_path: Path,
    path: str,
    mode: ProfileMode,
    report: ReportFormat,
    output: str | None,
    output_dir: str | None,
    template: str,
    sections: set[ReportSection],
    include: str | None,
    exclude: str | None,
    duration_seconds: float,
    config_file: str | None,
    verbosity: VerbosityLevel,
    preset: Optional[str] = None,
) -> ProfileMetadata:
    from aniwa import __version__
    
    include_sections = validate_sections(include)
    exclude_sections = validate_sections(exclude)

    return ProfileMetadata(
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        aniwa_version=__version__,
        python_version=platform.python_version(),
        operating_system=f"{platform.system()} {platform.release()}",
        polars_version=pl.__version__,
        dataset_path=str(dataset_path),
        dataset_file_type=dataset_path.suffix.lower().lstrip(".").upper(),
        dataset_size=format_file_size(dataset_path.stat().st_size),
        profiling_mode=mode.value,
        report_format=report.value,
        report_template=template if report in {ReportFormat.html, ReportFormat.pdf} else None,
        included_sections=include_sections or sorted(section.value for section in sections),
        excluded_sections=exclude_sections,
        profiling_duration=f"{duration_seconds:.2f}s",
        command_used=build_command_used(
            path=path,
            report=report,
            output=output,
            output_dir=output_dir,
            mode=mode,
            include=include,
            exclude=exclude,
            template=template,
            config_file=config_file,
            verbosity=verbosity,
            preset=preset,
        ),
    )


@app.command()
def profile(
    path: str = typer.Argument(..., help="Path to dataset file."),
    config_file: str | None = typer.Option(
        None,
        "--config",
        "-c",
        help="Path to configuration file.",
    ),
    preset: Optional[str] = typer.Option(
        None,
        "--preset",
        "-p",
        help="Profiling preset: quick, standard, audit, enterprise",
    ),
    report: ReportFormat | None = typer.Option(
        None,
        "--report",
        "-r",
        help="Report format.",
    ),
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path.",
    ),
    output_dir: str | None = typer.Option(
        None,
        "--output-dir",
        help="Output directory for generated report files.",
    ),
    mode: ProfileMode | None = typer.Option(
        None,
        "--mode",
        "-m",
        help="Profiling mode. Use 'fast' for lightweight checks or 'deep' for full profiling.",
    ),
    include: str | None = typer.Option(
        None,
        "--include",
        "-i",
        help="Comma-separated list of report sections to include.",
    ),
    exclude: str | None = typer.Option(
        None,
        "--exclude",
        "-e",
        help="Comma-separated list of report sections to exclude.",
    ),
    template: str | None = typer.Option(
        None,
        "--template",
        "-t",
        help="Report template for HTML/PDF outputs. Options: default, clean, compact, enterprise, dark.",
    ),
    verbosity: VerbosityLevel = typer.Option(
        VerbosityLevel.NORMAL,
        "--verbosity",
        help="Verbosity level: quiet, normal, verbose, debug",
    ),
):
    """
    Profile a dataset.
    """
    # Configure logging first thing
    configure_logger(verbosity)

    from aniwa import __version__

    logger = get_logger()
    
    # Log debug information
    log_debug("Starting Aniwa profiling", {
        "version": __version__,
        "python_version": platform.python_version(),
        "verbosity": verbosity.value,
        "preset": preset,
        "command": f"aniwa profile {path}",
    })
    
    # Load config file
    active_config = load_active_config(config_file)
    log_debug("Configuration loaded", active_config if verbosity == VerbosityLevel.DEBUG else None)
    
    # Apply preset if specified (before resolving other options)
    if preset:
        # Validate preset exists
        preset_obj = get_preset(preset)
        if not preset_obj:
            available_presets = ", ".join(list_presets().keys())
            raise typer.BadParameter(
                f"Unknown preset: '{preset}'. Available presets: {available_presets}"
            )
        
        # Collect CLI args that are not None
        cli_args = {}
        if mode is not None:
            cli_args["mode"] = mode.value
        if report is not None:
            cli_args["report"] = report.value
        if template is not None:
            cli_args["template"] = template
        if include is not None:
            cli_args["include"] = include
        if exclude is not None:
            cli_args["exclude"] = exclude
        if verbosity != VerbosityLevel.NORMAL:
            cli_args["verbosity"] = verbosity.value
        
        # Apply preset (preset values + CLI overrides)
        preset_config = apply_preset(preset, cli_args)
        log_debug(f"Applied preset: {preset}", preset_config)
        
        # Update active_config with preset values (CLI will still override later)
        for key, value in preset_config.items():
            if value is not None:
                active_config[key] = value

    # Resolve configuration (preset values are now in active_config)
    resolved_report = resolve_report_format(
        report if report is not None else active_config.get("report")
    )
    log_debug("Report format resolved", {"format": resolved_report.value})

    resolved_mode = resolve_profile_mode(
        mode if mode is not None else active_config.get("mode")
    )
    log_debug("Profiling mode resolved", {"mode": resolved_mode.value})

    resolved_template = (
        template
        if template is not None
        else active_config.get("template", "default")
    )
    log_debug("Template resolved", {"template": resolved_template})

    resolved_output = (
        output
        if output is not None
        else active_config.get("output")
    )

    resolved_output_dir = (
        output_dir
        if output_dir is not None
        else active_config.get("output_dir")
    )

    resolved_include = (
        include
        if include is not None
        else active_config.get("include")
    )

    resolved_exclude = (
        exclude
        if exclude is not None
        else active_config.get("exclude")
    )
    
    # Get verbosity from preset if not overridden by CLI
    if verbosity == VerbosityLevel.NORMAL and active_config.get("verbosity"):
        try:
            resolved_verbosity = VerbosityLevel(active_config.get("verbosity"))
            configure_logger(resolved_verbosity)
            logger = get_logger()
            verbosity = resolved_verbosity
        except ValueError:
            pass

    if include is not None:
        resolved_exclude = None

    if exclude is not None:
        resolved_include = None

    sections = resolve_sections(
        resolved_include,
        resolved_exclude,
    )
    
    log_debug("Sections resolved", {
        "sections": [s.value for s in sections],
        "include": resolved_include,
        "exclude": resolved_exclude,
    })

    final_output = resolve_output_path(
        output=resolved_output,
        output_dir=resolved_output_dir,
        report=resolved_report,
    )
    log_debug("Output path resolved", {"output": final_output})

    ensure_output_parent(final_output)

    dataset_path = Path(path)

    if not dataset_path.exists():
        log_error(f"File does not exist: {path}")
        raise typer.BadParameter(f"File does not exist: {path}")

    # Determine if we should show verbose progress (verbose or debug mode)
    show_verbose_progress = verbosity in [VerbosityLevel.VERBOSE, VerbosityLevel.DEBUG]
    
    # Initialize progress tracker
    tracker = ProgressTracker(verbose=show_verbose_progress)
    
    # Start profiling with progress tracking
    start_time = time.perf_counter()
    
    # Show reading dataset message based on verbosity
    if verbosity != VerbosityLevel.QUIET:
        log_info(f"Reading dataset: {path}")
    
    with tracker.stage("Reading dataset"):
        df = read_dataset(path)
        log_debug("Dataset loaded", {
            "rows": df.height,
            "columns": df.width,
            "shape": f"{df.height} x {df.width}",
        })
    
    if verbosity != VerbosityLevel.QUIET:
        log_info(f"Profiling dataset in {resolved_mode.value} mode")
    
    with tracker.stage(f"Profiling dataset in {resolved_mode.value} mode"):
        dataset_profile = profile_dataframe(
            df,
            mode=resolved_mode.value,
            sections=sections,
            verbose=show_verbose_progress,
        )
    
    duration_seconds = time.perf_counter() - start_time
    log_debug(f"Profiling completed in {duration_seconds:.2f}s")

    dataset_profile.metadata = build_profile_metadata(
        dataset_path=dataset_path,
        path=path,
        mode=resolved_mode,
        report=resolved_report,
        output=final_output if resolved_output else None,
        output_dir=resolved_output_dir,
        template=resolved_template,
        sections=sections,
        include=resolved_include,
        exclude=resolved_exclude,
        duration_seconds=duration_seconds,
        config_file=config_file,
        verbosity=verbosity,
        preset=preset,
    )

    # Report generation with progress tracking
    if resolved_report == ReportFormat.console:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating console report")
        with tracker.stage("Generating console report"):
            render_console_report(dataset_profile, verbose=show_verbose_progress)
        if verbosity != VerbosityLevel.QUIET:
            log_success("Console report generated")
        return

    if resolved_report == ReportFormat.json:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating JSON report")
        with tracker.stage("Generating JSON report"):
            json_output = render_json_report(dataset_profile, final_output)

            if final_output:
                if verbosity != VerbosityLevel.QUIET:
                    log_success(f"JSON report written to {final_output}")
            else:
                typer.echo(json_output)

        return

    if resolved_report == ReportFormat.html:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating HTML report")
        with tracker.stage("Generating HTML report"):
            try:
                render_html_report(dataset_profile, final_output, template=resolved_template)
            except ValueError as exc:
                log_error(f"Failed to generate HTML report: {exc}")
                raise typer.BadParameter(str(exc)) from exc

        if verbosity != VerbosityLevel.QUIET:
            log_success(f"HTML report written to {final_output}")
        return

    if resolved_report == ReportFormat.excel:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating Excel report")
        with tracker.stage("Generating Excel report"):
            try:
                render_excel_report(dataset_profile, final_output)
            except ValueError as exc:
                log_error(f"Failed to generate Excel report: {exc}")
                raise typer.BadParameter(str(exc)) from exc

        if verbosity != VerbosityLevel.QUIET:
            log_success(f"Excel report written to {final_output}")
        return

    if resolved_report == ReportFormat.markdown:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating Markdown report")
        with tracker.stage("Generating Markdown report"):
            markdown_output = render_markdown_report(dataset_profile, final_output)

            if final_output:
                if verbosity != VerbosityLevel.QUIET:
                    log_success(f"Markdown report written to {final_output}")
            else:
                typer.echo(markdown_output)

        return

    if resolved_report == ReportFormat.pdf:
        if verbosity != VerbosityLevel.QUIET:
            log_info("Generating PDF report")
        with tracker.stage("Generating PDF report"):
            try:
                render_pdf_report(dataset_profile, final_output, template=resolved_template)
            except ValueError as exc:
                log_error(f"Failed to generate PDF report: {exc}")
                raise typer.BadParameter(str(exc)) from exc

        if verbosity != VerbosityLevel.QUIET:
            log_success(f"PDF report written to {final_output}")
        return
    
    # Show final completion message (always in quiet mode, show in others)
    if verbosity == VerbosityLevel.QUIET:
        # Only show essential info in quiet mode
        console.print(f"{path}")
    else:
        console.print(f"\n[bold green]✓ Profiling complete for {path}[/bold green]")
        if final_output:
            console.print(f"[dim]Report saved to: {final_output}[/dim]")
    
    # Show timing summary in verbose or debug mode
    if show_verbose_progress:
        tracker.show_timing_summary()


@app.command(name="list-presets")
def list_presets_cmd():
    """List available profiling presets."""
    presets = list_presets()
    
    if not presets:
        console.print("[yellow]No presets available[/yellow]")
        return
    
    table = Table(title="Available Presets", border_style="cyan")
    table.add_column("Preset", style="bold cyan")
    table.add_column("Description", style="green")
    
    for name, description in presets.items():
        table.add_row(name, description)
    
    console.print(table)
    
    # Show usage example
    console.print("\n[dim]Usage example:[/dim]")
    console.print("[dim]  aniwa profile data.csv --preset quick[/dim]")
    console.print("[dim]  aniwa profile data.csv --preset enterprise --mode fast[/dim]")


if __name__ == "__main__":
    app()
