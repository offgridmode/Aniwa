from pathlib import Path

from typer.testing import CliRunner

from aniwa.cli import app


runner = CliRunner()


def write_csv(path: Path) -> None:
    path.write_text(
        "customer_id,name,email,revenue\n"
        "1,Ama,ama@example.com,1200\n"
        "2,Kofi,kofi@example.com,950\n"
        "3,Esi,,1100\n",
        encoding="utf-8",
    )


def test_cli_mutually_exclusive_include_exclude(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--include",
            "summary",
            "--exclude",
            "statistics",
        ],
    )

    assert result.exit_code != 0
    assert "Use either --include or --exclude, not both" in result.output


def test_cli_invalid_include_section(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--include",
            "invalid_section",
        ],
    )

    assert result.exit_code != 0
    assert "Invalid report section: invalid_section" in result.output


def test_cli_invalid_exclude_section(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--exclude",
            "unknown_block",
        ],
    )

    assert result.exit_code != 0
    assert "Invalid report section: unknown_block" in result.output


def test_cli_json_include_summary_only(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "json",
            "--include",
            "summary",
        ],
    )

    assert result.exit_code == 0
    assert '"summary"' in result.output
    assert '"rows"' in result.output
    assert '"columns"' in result.output
    assert '"quality"' not in result.output
    assert '"insights"' not in result.output


def test_cli_json_include_summary_and_insights(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "json",
            "--include",
            "summary,insights",
        ],
    )

    assert result.exit_code == 0
    assert '"summary"' in result.output
    assert '"insights"' in result.output
    assert '"quality"' not in result.output


def test_cli_json_exclude_statistics(tmp_path):
    csv_path = tmp_path / "customers.csv"
    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "json",
            "--exclude",
            "statistics",
        ],
    )

    assert result.exit_code == 0
    assert '"summary"' in result.output
    assert '"quality"' in result.output
    assert '"insights"' in result.output
    assert '"numeric_stats"' not in result.output


def test_cli_html_include_summary_and_insights(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "summary_insights.html"

    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "html",
            "--include",
            "summary,insights",
            "--output",
            str(output_path),
        ],
    )

    assert result.exit_code == 0
    assert output_path.exists()

    html = output_path.read_text(encoding="utf-8")

    assert "Rows" in html
    assert "Columns" in html
    assert "Insights" in html
    assert "Duplicate Rows" not in html
    assert "Column Profile" not in html
    assert "Numeric Statistics" not in html


def test_cli_html_include_summary_only(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "summary_only.html"

    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "html",
            "--include",
            "summary",
            "--output",
            str(output_path),
        ],
    )

    assert result.exit_code == 0
    assert output_path.exists()

    html = output_path.read_text(encoding="utf-8")

    assert "Rows" in html
    assert "Columns" in html
    assert "Duplicate Rows" not in html
    assert "Column Profile" not in html
    assert "Charts" not in html
    assert "Insights" not in html


def test_cli_html_exclude_quality(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "exclude_quality.html"

    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "html",
            "--exclude",
            "quality",
            "--output",
            str(output_path),
        ],
    )

    assert result.exit_code == 0
    assert output_path.exists()

    html = output_path.read_text(encoding="utf-8")

    assert "Rows" in html
    assert "Columns" in html
    assert "Duplicate Rows" not in html
    assert "Column Profile" in html
    assert "Insights" in html


def test_cli_html_exclude_charts(tmp_path):
    csv_path = tmp_path / "customers.csv"
    output_path = tmp_path / "exclude_charts.html"

    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "html",
            "--exclude",
            "charts",
            "--output",
            str(output_path),
        ],
    )

    assert result.exit_code == 0
    assert output_path.exists()

    html = output_path.read_text(encoding="utf-8")

    assert "Rows" in html
    assert "Columns" in html
    assert "Column Profile" in html
    assert "Charts" not in html
    assert "aniwa-default-chart-data" not in html


def test_cli_markdown_include_summary_only(tmp_path):
    csv_path = tmp_path / "customers.csv"

    write_csv(csv_path)

    result = runner.invoke(
        app,
        [
            str(csv_path),
            "--report",
            "markdown",
            "--include",
            "summary",
        ],
    )

    assert result.exit_code == 0
    assert "## Summary" in result.output
    assert "## Columns" not in result.output
    assert "## Data Quality" not in result.output
    assert "## Insights" not in result.output