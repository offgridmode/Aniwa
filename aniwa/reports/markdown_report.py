from pathlib import Path
from aniwa.models.profile import DatasetProfile

def render_markdown_report(profile: DatasetProfile, output: str | None = None) -> str:
    sections = [
        _render_summary(profile),
        _render_columns(profile),
        _render_numeric_stats(profile),
        _render_quality(profile),
        _render_insights(profile)
    ]
    
    markdown_content = "\n\n".join(filter(None, sections))
    
    if output:
        Path(output).parent.mkdir(parents=True, exist_ok=True)
        Path(output).write_text(markdown_content, encoding="utf-8")
        return f"Markdown report written to {output}"
    
    return markdown_content

def _render_summary(profile: DatasetProfile) -> str:
    if not profile.summary:
        return "## Summary\nNot available"
    return (f"## Summary\n| Metric | Value |\n| --- | --- |\n"
            f"| Rows | {profile.summary.rows} |\n"
            f"| Columns | {profile.summary.columns} |")

def _render_columns(profile: DatasetProfile) -> str:
    if not profile.columns:
        return ""
    
    header = "| Column | Type | Null % | Unique |\n| --- | --- | --- | --- |"
    rows = []
    for col in profile.columns:
        rows.append(f"| {col.name} | {col.dtype} | {col.null_percent:.2f}% | {col.unique_count} |")
    
    return "## Columns\n" + header + "\n" + "\n".join(rows)

def _render_numeric_stats(profile: DatasetProfile) -> str:

    if not profile.columns:
        return ""
    
    numeric_cols = [col for col in profile.columns if col.numeric_stats]
    
    if not numeric_cols:
        return ""

    header = "| Column | Min | Max | Mean | Median | Std |\n| --- | --- | --- | --- | --- | --- |"
    rows = []
    for col in numeric_cols:
        assert col.numeric_stats is not None  
        stats = col.numeric_stats
        rows.append(f"| {col.name} | {stats.min} | {stats.max} | {stats.mean:.2f} | {stats.median} | {stats.std:.2f} |")
    
    return "## Numeric Statistics\n" + header + "\n" + "\n".join(rows)

def _render_quality(profile: DatasetProfile) -> str:
    if not profile.quality:
        return ""
    return (f"## Data Quality\n- **Duplicate Rows:** {profile.quality.duplicate_rows}\n"
            f"- **Duplicate %:** {profile.quality.duplicate_percent}")


def _render_insights(profile: DatasetProfile) -> str:
    if not profile.insights:
        return "## Insights\nNo major issues detected."
    
    rows = [f"| {i.level} | {i.message} |" for i in profile.insights]
    return "## Insights\n| Level | Message |\n| --- | --- |\n" + "\n".join(rows)