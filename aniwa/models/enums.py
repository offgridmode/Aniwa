from enum import Enum

class ReportSection(str, Enum):
    summary = "summary"
    columns = "columns"
    quality = "quality"
    insights = "insights"