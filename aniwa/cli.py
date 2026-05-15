from enum import Enum
from pathlib import Path

import typer

from aniwa.io.readers import read_dataset
from aniwa.core.profiler import profile_dataframe
from aniwa.reports.console import render_console_report
from aniwa.reports.json_report import render_json_report


app = typer.Typer(help="Aniwa — Universal dataset profiling and intelligence.")


class ReportFormat(str, Enum):
    console = "console"
    json = "json"


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
):
    """
    Profile a dataset.
    """
    dataset_path = Path(path)

    if not dataset_path.exists():
        raise typer.BadParameter(f"File does not exist: {path}")

    df = read_dataset(path)
    dataset_profile = profile_dataframe(df)

    if report == ReportFormat.console:
        render_console_report(dataset_profile)

    elif report == ReportFormat.json:
        json_output = render_json_report(dataset_profile, output)

        if not output:
            typer.echo(json_output)