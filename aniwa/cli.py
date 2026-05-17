from enum import Enum
from pathlib import Path

import typer

from aniwa.core.profiler import profile_dataframe
from aniwa.io.readers import read_dataset
from aniwa.reports.console import render_console_report
from aniwa.reports.html_report import render_html_report
from aniwa.reports.json_report import render_json_report
from aniwa.models.enums import ReportSection

app = typer.Typer(help="Aniwa — Universal dataset profiling and intelligence.")


class ReportFormat(str, Enum):
    console = "console"
    json = "json"
    html = "html"


class ProfileMode(str, Enum):
    fast = "fast"
    deep = "deep"

def validate_sections(value: str | None) -> list[str] | None:
    if not value:
        return None

    split_sections = [item.strip() for item in value.split(",")]
    valid_options = [e.value for e in ReportSection]

    for sec in split_sections:
        if sec not in valid_options:
            raise typer.BadParameter(f"Invalid report section: {sec}. Valid options are: {', '.join(valid_options)}.")

    return split_sections

@app.command()
def profile(
    path: str = typer.Argument(..., help="Path to dataset file."),
    report: ReportFormat = typer.Option(
        ReportFormat.console,
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
    mode: ProfileMode = typer.Option(
        ProfileMode.deep,
        "--mode",
        "-m",
        help="Profiling mode. Use 'fast' for lightweight checks or 'deep' for full profiling.",
    ),
    include: str | None = typer.Option(
        None,
        "--include",
        "-i",
        help="Comma-separated list of columns to include in the report.",
    ),
    exclude: str | None = typer.Option(
        None,
        "--exclude",
        "-e",
        help="Comma-separated list of columns to exclude from the report.",
    )
):
    """
    Profile a dataset.
    """
    include = validate_sections(include)
    exclude = validate_sections(exclude)

    sections: list[str] | None = None

    if include or exclude:
        sections = []
        base = [e.value for e in ReportSection] if not include else include

        for item in base:
            if item not in (exclude or []):
                sections.append(item)

    dataset_path = Path(path)

    if not dataset_path.exists():
        raise typer.BadParameter(f"File does not exist: {path}")

    df = read_dataset(path)
    dataset_profile = profile_dataframe(df, mode=mode.value, sections=sections)

    if report == ReportFormat.console:
        render_console_report(dataset_profile)
        return

    if report == ReportFormat.json:
        json_output = render_json_report(dataset_profile, output)

        if output:
            typer.echo(f"JSON report written to {output}")
        else:
            typer.echo(json_output)

        return

    if report == ReportFormat.html:
        if output is None:
            output = "aniwa_report.html"

        render_html_report(dataset_profile, output)
        typer.echo(f"HTML report written to {output}")
        return