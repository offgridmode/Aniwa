"""Profiling presets for Aniwa."""

from typing import Dict, Any, Optional, Set
from dataclasses import dataclass
from aniwa.models.enums import ReportSection
from aniwa.utils.logging import get_logger, log_debug


@dataclass
class Preset:
    """Configuration preset for profiling workflow."""
    
    name: str
    description: str
    mode: str  # "fast" or "deep"
    report_format: Optional[str] = None
    template: Optional[str] = None
    include_sections: Optional[Set[ReportSection]] = None
    exclude_sections: Optional[Set[ReportSection]] = None
    verbosity: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert preset to dictionary for merging with CLI args."""
        result = {}
        
        if self.mode:
            result["mode"] = self.mode
        if self.report_format:
            result["report"] = self.report_format
        if self.template:
            result["template"] = self.template
        if self.include_sections:
            result["include"] = ",".join(s.value for s in self.include_sections)
        if self.exclude_sections:
            result["exclude"] = ",".join(s.value for s in self.exclude_sections)
        if self.verbosity:
            result["verbosity"] = self.verbosity
        
        return result


# Built-in preset definitions
BUILTIN_PRESETS: Dict[str, Preset] = {
    "quick": Preset(
        name="quick",
        description="Fast lightweight profiling for quick data inspection",
        mode="fast",
        include_sections={
            ReportSection.summary,
            ReportSection.schema,
            ReportSection.quality,
        },
        exclude_sections={
            ReportSection.statistics,
            ReportSection.insights,
            ReportSection.charts,
        },
    ),
    
    "standard": Preset(
        name="standard",
        description="Balanced default profiling with statistics and insights",
        mode="deep",
        include_sections={
            ReportSection.summary,
            ReportSection.schema,
            ReportSection.quality,
            ReportSection.statistics,
            ReportSection.insights,
        },
        exclude_sections={
            ReportSection.charts,
        },
    ),
    
    "audit": Preset(
        name="audit",
        description="Comprehensive profiling for validation and audit workflows",
        mode="deep",
        report_format="html",
        template="enterprise",
        include_sections={
            ReportSection.summary,
            ReportSection.schema,
            ReportSection.quality,
            ReportSection.statistics,
            ReportSection.insights,
            ReportSection.charts,
        },
        verbosity="verbose",
    ),
    
    "enterprise": Preset(
        name="enterprise",
        description="Professional branded reporting for stakeholders",
        mode="deep",
        report_format="html",
        template="enterprise",
        include_sections={
            ReportSection.summary,
            ReportSection.schema,
            ReportSection.quality,
            ReportSection.statistics,
            ReportSection.insights,
            ReportSection.charts,
        },
        verbosity="normal",
    ),
}


def get_preset(preset_name: str) -> Optional[Preset]:
    """Get a built-in preset by name.
    
    Args:
        preset_name: Name of the preset (quick, standard, audit, enterprise)
    
    Returns:
        Preset object if found, None otherwise
    """
    return BUILTIN_PRESETS.get(preset_name.lower())


def list_presets() -> Dict[str, str]:
    """List all available presets with their descriptions.
    
    Returns:
        Dictionary mapping preset names to descriptions
    """
    return {name: preset.description for name, preset in BUILTIN_PRESETS.items()}


def apply_preset(
    preset_name: str,
    cli_args: Dict[str, Any],
) -> Dict[str, Any]:
    """Apply preset configuration and merge with CLI arguments.
    
    CLI arguments take precedence over preset values.
    
    Args:
        preset_name: Name of the preset to apply
        cli_args: Dictionary of CLI arguments (only non-None values)
    
    Returns:
        Merged configuration dictionary
    """
    logger = get_logger()
    
    preset = get_preset(preset_name)
    if not preset:
        raise ValueError(f"Unknown preset: '{preset_name}'. Available presets: {', '.join(list_presets().keys())}")
    
    log_debug(f"Applying preset: {preset_name}", {
        "name": preset.name,
        "description": preset.description,
        "mode": preset.mode,
        "report_format": preset.report_format,
        "template": preset.template,
        "include_sections": [s.value for s in preset.include_sections] if preset.include_sections else None,
        "exclude_sections": [s.value for s in preset.exclude_sections] if preset.exclude_sections else None,
        "verbosity": preset.verbosity,
    })
    
    # Start with preset values
    result = preset.to_dict()
    
    # Override with CLI arguments (only non-None values)
    for key, value in cli_args.items():
        if value is not None:
            result[key] = value
            log_debug(f"CLI override: {key} = {value}")
    
    # Handle special case: if both include and exclude are present, exclude wins
    if "include" in result and "exclude" in result:
        log_debug("Both include and exclude present, excluding exclude sections from include")
        # This will be handled by resolve_sections in cli.py
    
    return result


def validate_preset_compatibility(
    preset_name: str,
    mode: Optional[str] = None,
    report: Optional[str] = None,
    template: Optional[str] = None,
    include: Optional[str] = None,
    exclude: Optional[str] = None,
    verbosity: Optional[str] = None,
) -> None:
    """Validate that preset and CLI arguments are compatible.
    
    Args:
        preset_name: Name of the preset
        mode: Profiling mode from CLI
        report: Report format from CLI
        template: Template name from CLI
        include: Include sections from CLI
        exclude: Exclude sections from CLI
        verbosity: Verbosity level from CLI
    
    Raises:
        ValueError: If incompatible combinations are found
    """
    preset = get_preset(preset_name)
    if not preset:
        return
    
    # Check for incompatible combinations
    if preset.report_format == "console" and report and report != "console":
        log_debug(f"Preset report format '{preset.report_format}' overridden by CLI '{report}'")
    
    if preset.template and template and preset.template != template:
        log_debug(f"Preset template '{preset.template}' overridden by CLI '{template}'")
    
    if preset.mode and mode and preset.mode != mode:
        log_debug(f"Preset mode '{preset.mode}' overridden by CLI '{mode}'")
    
    if preset.verbosity and verbosity and preset.verbosity != verbosity:
        log_debug(f"Preset verbosity '{preset.verbosity}' overridden by CLI '{verbosity}'")