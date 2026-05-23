from enum import Enum


class ReportSection(str, Enum):
    summary = "summary"
    schema = "schema"
    quality = "quality"
    statistics = "statistics"
    insights = "insights"
    charts = "charts"