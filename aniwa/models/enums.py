from enum import Enum


class ReportSection(str, Enum):
    summary = "summary"
    schema = "schema"
    quality = "quality"
    statistics = "statistics"
    insights = "insights"
    charts = "charts"


class PresetType(str, Enum):
    """Built-in presets for Aniwa profiling workflows."""
    
    QUICK = "quick"          # Fast lightweight profiling
    STANDARD = "standard"    # Balanced default profiling
    AUDIT = "audit"         # For validation and audit workflows
    ENTERPRISE = "enterprise"  # Professional branded reporting