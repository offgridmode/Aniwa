import tempfile
from typer.testing import CliRunner

from aniwa.cli import app

runner = CliRunner()

def test_cli_mutually_exclusive_include_exclude():
    with tempfile.NamedTemporaryFile(suffix=".csv") as f:
        result = runner.invoke(
            app, [f.name, "--include", "summary", "--exclude", "statistics"]
        )
        assert result.exit_code != 0
        assert "Use either --include or --exclude, not both" in result.output

def test_cli_invalid_include_section():
    with tempfile.NamedTemporaryFile(suffix=".csv") as f:
        result = runner.invoke(app, [f.name, "--include", "invalid_section"])
        assert result.exit_code != 0
        assert "Invalid report section: invalid_section" in result.output

def test_cli_invalid_exclude_section():
    with tempfile.NamedTemporaryFile(suffix=".csv") as f:
        result = runner.invoke(app, [f.name, "--exclude", "unknown_block"])
        assert result.exit_code != 0
        assert "Invalid report section: unknown_block" in result.output