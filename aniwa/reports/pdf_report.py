from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from aniwa.charts.pdf_charts import (
    generate_cardinality_chart,
    generate_duplicate_chart,
    generate_null_chart,
)
from aniwa.models.profile import DatasetProfile


PDF_THEMES = {
    "default": {
        "page_bg": "#f8fafc",
        "text": "#0f172a",
        "muted": "#64748b",
        "metadata": "#0891b2",
        "summary": "#2563eb",
        "schema": "#0f172a",
        "statistics": "#7c3aed",
        "insights": "#ca8a04",
        "body_bg": "#ffffff",
        "row_alt": "#f8fafc",
        "grid": "#e2e8f0",
    },
    "clean": {
        "page_bg": "#ffffff",
        "text": "#111827",
        "muted": "#6b7280",
        "metadata": "#374151",
        "summary": "#111827",
        "schema": "#374151",
        "statistics": "#4b5563",
        "insights": "#6b7280",
        "body_bg": "#ffffff",
        "row_alt": "#f9fafb",
        "grid": "#e5e7eb",
    },
    "compact": {
        "page_bg": "#ffffff",
        "text": "#111827",
        "muted": "#6b7280",
        "metadata": "#475569",
        "summary": "#334155",
        "schema": "#1f2937",
        "statistics": "#475569",
        "insights": "#64748b",
        "body_bg": "#ffffff",
        "row_alt": "#f8fafc",
        "grid": "#e5e7eb",
    },
    "enterprise": {
        "page_bg": "#eff6ff",
        "text": "#172554",
        "muted": "#475569",
        "metadata": "#1e3a8a",
        "summary": "#1d4ed8",
        "schema": "#1e3a8a",
        "statistics": "#0f766e",
        "insights": "#92400e",
        "body_bg": "#ffffff",
        "row_alt": "#eff6ff",
        "grid": "#bfdbfe",
    },
    "dark": {
        "page_bg": "#020617",
        "text": "#e5e7eb",
        "muted": "#94a3b8",
        "metadata": "#0891b2",
        "summary": "#0f172a",
        "schema": "#1e293b",
        "statistics": "#334155",
        "insights": "#0369a1",
        "body_bg": "#0f172a",
        "row_alt": "#111827",
        "grid": "#334155",
    },
}


def render_pdf_report(
    profile: DatasetProfile,
    output: str,
    template: str = "default",
) -> None:
    theme = _get_theme(template)
    output_path = Path(output)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=landscape(letter),
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()
    styles["Title"].textColor = colors.HexColor(theme["text"])
    styles["Heading2"].textColor = colors.HexColor(theme["text"])
    styles["BodyText"].textColor = colors.HexColor(theme["muted"])
    styles["Italic"].textColor = colors.HexColor(theme["muted"])

    elements = []

    elements.append(Paragraph("Aniwa Dataset Profile", styles["Title"]))
    elements.append(
        Paragraph(
            "Universal dataset profiling and intelligence report.",
            styles["BodyText"],
        )
    )
    elements.append(Spacer(1, 20))

    if profile.metadata:
        elements.append(Paragraph("Profiling Metadata", styles["Heading2"]))
        metadata_table = Table(_build_metadata_data(profile), colWidths=[180, 520])
        _style_table(metadata_table, header_color=theme["metadata"], theme=theme)
        elements.append(metadata_table)
        elements.append(Spacer(1, 24))

    if profile.summary or profile.quality:
        elements.append(Paragraph("Dataset Summary", styles["Heading2"]))

        summary_data = [["Metric", "Value"]]

        if profile.summary:
            summary_data.append(["Rows", f"{profile.summary.rows:,}"])
            summary_data.append(["Columns", f"{profile.summary.columns:,}"])

        if profile.quality:
            summary_data.append(
                ["Duplicate Rows", f"{profile.quality.duplicate_rows:,}"]
            )
            summary_data.append(
                ["Duplicate %", f"{profile.quality.duplicate_percent}%"]
            )

        summary_table = Table(summary_data, colWidths=[200, 200])
        _style_table(summary_table, header_color=theme["summary"], theme=theme)
        elements.append(summary_table)
        elements.append(Spacer(1, 24))

    if profile.columns:
        _render_charts(elements, profile, styles)

        elements.append(Paragraph("Schema Profile", styles["Heading2"]))

        column_data = [["Column", "Type", "Nulls", "Null %", "Unique"]]

        for col in profile.columns:
            column_data.append(
                [
                    col.name,
                    col.dtype,
                    f"{col.null_count:,}",
                    f"{col.null_percent}%",
                    f"{col.unique_count:,}",
                ]
            )

        column_table = Table(column_data, repeatRows=1)
        _style_table(column_table, header_color=theme["schema"], theme=theme)
        elements.append(column_table)
        elements.append(Spacer(1, 24))

        numeric_columns = [col for col in profile.columns if col.numeric_stats]

        if numeric_columns:
            elements.append(Paragraph("Numeric Statistics", styles["Heading2"]))

            stats_data = [["Column", "Min", "Max", "Mean", "Median", "Std"]]

            for col in numeric_columns:
                stats = col.numeric_stats
                stats_data.append(
                    [
                        col.name,
                        _format_value(stats.min),
                        _format_value(stats.max),
                        _format_value(stats.mean),
                        _format_value(stats.median),
                        _format_value(stats.std),
                    ]
                )

            stats_table = Table(stats_data, repeatRows=1)
            _style_table(stats_table, header_color=theme["statistics"], theme=theme)
            elements.append(stats_table)
            elements.append(Spacer(1, 24))

    if profile.insights:
        elements.append(Paragraph("Insights", styles["Heading2"]))

        insight_data = [["Level", "Message"]]

        for insight in profile.insights:
            insight_data.append([insight.level.upper(), insight.message])

        insight_table = Table(insight_data, colWidths=[120, 620], repeatRows=1)
        _style_table(insight_table, header_color=theme["insights"], theme=theme)
        elements.append(insight_table)

    elements.append(Spacer(1, 24))
    elements.append(
        Paragraph(
            "Generated by Aniwa - See your data clearly.",
            styles["Italic"],
        )
    )

    doc.build(
        elements,
        onFirstPage=lambda canvas, doc: _draw_page_background(canvas, doc, theme),
        onLaterPages=lambda canvas, doc: _draw_page_background(canvas, doc, theme),
    )


def _render_charts(
    elements: list,
    profile: DatasetProfile,
    styles,
) -> None:
    elements.append(Paragraph("Charts", styles["Heading2"]))
    elements.append(Spacer(1, 12))

    null_chart = generate_null_chart(profile)
    cardinality_chart = generate_cardinality_chart(profile)
    duplicate_chart = generate_duplicate_chart(profile)

    elements.append(Paragraph("Null Percentage by Column", styles["BodyText"]))
    elements.append(Spacer(1, 8))
    elements.append(Image(null_chart, width=420, height=220))
    elements.append(Spacer(1, 24))

    elements.append(Paragraph("Unique Values by Column", styles["BodyText"]))
    elements.append(Spacer(1, 8))
    elements.append(Image(cardinality_chart, width=420, height=220))
    elements.append(Spacer(1, 24))

    if profile.summary and profile.quality:
        elements.append(Paragraph("Duplicate Overview", styles["BodyText"]))
        elements.append(Spacer(1, 8))
        elements.append(Image(duplicate_chart, width=320, height=320))
        elements.append(Spacer(1, 30))


def _build_metadata_data(profile: DatasetProfile) -> list[list[str]]:
    if not profile.metadata:
        return [["Field", "Value"]]

    metadata = profile.metadata
    rows = [["Field", "Value"]]

    _add_metadata_row(rows, "Generated At", metadata.generated_at)

    _add_metadata_row(rows, "Aniwa Version", metadata.aniwa_version)
    _add_metadata_row(rows, "Python Version", metadata.python_version)
    _add_metadata_row(rows, "Operating System", metadata.operating_system)
    _add_metadata_row(rows, "Polars Version", metadata.polars_version)

    _add_metadata_row(rows, "Dataset Path", metadata.dataset_path)
    _add_metadata_row(rows, "Dataset File Type", metadata.dataset_file_type)
    _add_metadata_row(rows, "Dataset Size", metadata.dataset_size)

    _add_metadata_row(rows, "Profiling Mode", metadata.profiling_mode)
    _add_metadata_row(rows, "Report Format", metadata.report_format)
    _add_metadata_row(rows, "Report Template", metadata.report_template)

    if metadata.included_sections:
        _add_metadata_row(
            rows,
            "Included Sections",
            ", ".join(metadata.included_sections),
        )

    if metadata.excluded_sections:
        _add_metadata_row(
            rows,
            "Excluded Sections",
            ", ".join(metadata.excluded_sections),
        )

    _add_metadata_row(rows, "Profiling Duration", metadata.profiling_duration)
    _add_metadata_row(rows, "Command Used", metadata.command_used)

    return rows


def _add_metadata_row(
    rows: list[list[str]],
    field: str,
    value: str | None,
) -> None:
    if value is None:
        return

    rows.append([field, value])


def _get_theme(template: str) -> dict[str, str]:
    theme = PDF_THEMES.get(template)

    if theme is None:
        valid_templates = ", ".join(PDF_THEMES)
        raise ValueError(
            f"Invalid PDF report template: {template}. "
            f"Valid templates are: {valid_templates}."
        )

    return theme


def _draw_page_background(canvas, doc, theme: dict[str, str]) -> None:
    canvas.saveState()
    canvas.setFillColor(colors.HexColor(theme["page_bg"]))
    canvas.rect(
        0,
        0,
        doc.pagesize[0],
        doc.pagesize[1],
        fill=1,
        stroke=0,
    )
    canvas.restoreState()


def _style_table(
    table: Table,
    header_color: str,
    theme: dict[str, str],
) -> None:
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_color)),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor(theme["grid"])),
                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [
                        colors.HexColor(theme["body_bg"]),
                        colors.HexColor(theme["row_alt"]),
                    ],
                ),
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.HexColor(theme["text"])),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("TOPPADDING", (0, 0), (-1, 0), 10),
            ]
        )
    )


def _format_value(value: float | None) -> str:
    if value is None:
        return "-"

    if float(value).is_integer():
        return f"{int(value):,}"

    return f"{value:,.4f}"