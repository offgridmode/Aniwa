"""Tests for profiling presets."""

import pytest
from unittest.mock import Mock, patch
from aniwa.models.enums import ReportSection, PresetType
from aniwa.presets import (
    Preset,
    get_preset,
    list_presets,
    apply_preset,
    validate_preset_compatibility,
    BUILTIN_PRESETS,
)


def test_builtin_presets_exist():
    """Test that all built-in presets are defined."""
    expected_presets = ["quick", "standard", "audit", "enterprise"]
    for preset_name in expected_presets:
        assert get_preset(preset_name) is not None


def test_quick_preset():
    """Test quick preset configuration."""
    preset = get_preset("quick")
    assert preset is not None
    assert preset.name == "quick"
    assert preset.mode == "fast"
    assert preset.description is not None
    assert preset.include_sections is not None
    assert ReportSection.summary in preset.include_sections
    assert ReportSection.schema in preset.include_sections
    assert ReportSection.quality in preset.include_sections
    assert ReportSection.statistics not in preset.include_sections
    assert ReportSection.insights not in preset.include_sections
    assert ReportSection.charts not in preset.include_sections


def test_standard_preset():
    """Test standard preset configuration."""
    preset = get_preset("standard")
    assert preset is not None
    assert preset.name == "standard"
    assert preset.mode == "deep"
    assert preset.include_sections is not None
    assert ReportSection.summary in preset.include_sections
    assert ReportSection.schema in preset.include_sections
    assert ReportSection.quality in preset.include_sections
    assert ReportSection.statistics in preset.include_sections
    assert ReportSection.insights in preset.include_sections
    assert ReportSection.charts not in preset.include_sections


def test_audit_preset():
    """Test audit preset configuration."""
    preset = get_preset("audit")
    assert preset is not None
    assert preset.name == "audit"
    assert preset.mode == "deep"
    assert preset.report_format == "html"
    assert preset.template == "enterprise"
    assert preset.verbosity == "verbose"
    assert preset.include_sections is not None
    assert ReportSection.summary in preset.include_sections
    assert ReportSection.schema in preset.include_sections
    assert ReportSection.quality in preset.include_sections
    assert ReportSection.statistics in preset.include_sections
    assert ReportSection.insights in preset.include_sections
    assert ReportSection.charts in preset.include_sections


def test_enterprise_preset():
    """Test enterprise preset configuration."""
    preset = get_preset("enterprise")
    assert preset is not None
    assert preset.name == "enterprise"
    assert preset.mode == "deep"
    assert preset.report_format == "html"
    assert preset.template == "enterprise"
    assert preset.verbosity == "normal"
    assert preset.include_sections is not None
    assert ReportSection.summary in preset.include_sections
    assert ReportSection.schema in preset.include_sections
    assert ReportSection.quality in preset.include_sections
    assert ReportSection.statistics in preset.include_sections
    assert ReportSection.insights in preset.include_sections
    assert ReportSection.charts in preset.include_sections


def test_list_presets():
    """Test listing presets."""
    presets = list_presets()
    assert "quick" in presets
    assert "standard" in presets
    assert "audit" in presets
    assert "enterprise" in presets
    assert len(presets) == 4
    assert "Fast lightweight profiling for quick data inspection" in presets["quick"]
    assert "Balanced default profiling with statistics and insights" in presets["standard"]


def test_apply_preset_without_overrides():
    """Test applying preset without CLI overrides."""
    result = apply_preset("quick", {})
    assert result["mode"] == "fast"
    assert "include" in result
    assert "exclude" in result
    assert result["include"] == "summary,schema,quality"
    assert result["exclude"] == "statistics,insights,charts"


def test_apply_preset_with_cli_override():
    """Test applying preset with CLI overrides."""
    cli_args = {"mode": "deep"}
    result = apply_preset("quick", cli_args)
    assert result["mode"] == "deep"  # CLI overrides preset
    assert "include" in result  # Preset values still present
    assert result["include"] == "summary,schema,quality"


def test_apply_preset_with_multiple_overrides():
    """Test applying preset with multiple CLI overrides."""
    cli_args = {
        "mode": "fast",
        "report": "json",
        "verbosity": "quiet"
    }
    result = apply_preset("standard", cli_args)
    assert result["mode"] == "fast"
    assert result["report"] == "json"
    assert result["verbosity"] == "quiet"
    assert "include" in result
    assert "exclude" in result


def test_apply_preset_invalid():
    """Test applying invalid preset."""
    with pytest.raises(ValueError, match="Unknown preset"):
        apply_preset("invalid_preset", {})


def test_preset_to_dict():
    """Test preset to dictionary conversion."""
    preset = get_preset("quick")
    preset_dict = preset.to_dict()
    assert preset_dict["mode"] == "fast"
    assert "include" in preset_dict
    assert "exclude" in preset_dict
    assert preset_dict["include"] == "summary,schema,quality"
    assert preset_dict["exclude"] == "statistics,insights,charts"


def test_preset_to_dict_with_optional_fields():
    """Test preset to dictionary conversion with optional fields."""
    preset = get_preset("audit")
    preset_dict = preset.to_dict()
    assert preset_dict["mode"] == "deep"
    assert preset_dict["report"] == "html"
    assert preset_dict["template"] == "enterprise"
    assert preset_dict["verbosity"] == "verbose"


def test_case_insensitive_preset_lookup():
    """Test that preset lookup is case-insensitive."""
    preset_lower = get_preset("quick")
    preset_upper = get_preset("QUICK")
    preset_mixed = get_preset("Quick")
    
    assert preset_lower is not None
    assert preset_upper is not None
    assert preset_mixed is not None
    assert preset_lower.name == preset_upper.name
    assert preset_lower.name == preset_mixed.name


def test_validate_preset_compatibility_no_conflicts():
    """Test preset compatibility validation with no conflicts."""
    # Should not raise any exception
    validate_preset_compatibility("quick")
    validate_preset_compatibility("standard", mode="deep")
    validate_preset_compatibility("audit", report="html")


def test_preset_compatibility_with_overrides():
    """Test preset compatibility validation with overrides."""
    # These should not raise exceptions (overrides are allowed)
    validate_preset_compatibility("quick", mode="deep")
    validate_preset_compatibility("enterprise", report="json")
    validate_preset_compatibility("audit", verbosity="quiet")


def test_preset_objects_are_unique():
    """Test that each preset is a unique object."""
    quick1 = get_preset("quick")
    quick2 = get_preset("quick")
    standard = get_preset("standard")
    
    assert quick1 is quick2  # Same object reference
    assert quick1 is not standard  # Different presets are different objects


def test_preset_include_exclude_mutually_exclusive():
    """Test that presets don't have both include and exclude by default."""
    for preset_name in ["quick", "standard", "audit", "enterprise"]:
        preset = get_preset(preset_name)
        # Should have either include or exclude sections, not both in the config
        assert (preset.include_sections is not None) or (preset.exclude_sections is not None)


def test_all_sections_defined():
    """Test that all ReportSection values are handled."""
    all_sections = set(ReportSection)
    for preset_name in ["quick", "standard", "audit", "enterprise"]:
        preset = get_preset(preset_name)
        if preset.include_sections:
            for section in preset.include_sections:
                assert section in all_sections
        if preset.exclude_sections:
            for section in preset.exclude_sections:
                assert section in all_sections


def test_apply_preset_returns_dict():
    """Test that apply_preset returns a dictionary."""
    result = apply_preset("quick", {})
    assert isinstance(result, dict)
    assert len(result) > 0


def test_apply_preset_preserves_cli_values():
    """Test that CLI values are preserved when applying preset."""
    cli_args = {
        "mode": "fast",
        "report": "json",
        "template": "dark",
        "verbosity": "debug"
    }
    result = apply_preset("enterprise", cli_args)
    
    # CLI values should be in result
    assert result["mode"] == "fast"
    assert result["report"] == "json"
    assert result["template"] == "dark"
    assert result["verbosity"] == "debug"


def test_get_preset_nonexistent():
    """Test getting a nonexistent preset."""
    assert get_preset("nonexistent") is None
    assert get_preset("") is None


def test_list_presets_returns_dict():
    """Test that list_presets returns a dictionary."""
    presets = list_presets()
    assert isinstance(presets, dict)
    assert len(presets) == 4


@patch('aniwa.presets.log_debug')
def test_apply_preset_logging(mock_log_debug):
    """Test that apply_preset logs debug information."""
    result = apply_preset("quick", {"mode": "deep"})
    assert mock_log_debug.called
    mock_log_debug.assert_any_call("Applying preset: quick", {
        "name": "quick",
        "description": "Fast lightweight profiling for quick data inspection",
        "mode": "fast",
        "report_format": None,
        "template": None,
        "include_sections": ["summary", "schema", "quality"],
        "exclude_sections": ["statistics", "insights", "charts"],
        "verbosity": None,
    })
    mock_log_debug.assert_any_call("CLI override: mode = deep")


def test_preset_data_class():
    """Test Preset dataclass initialization."""
    preset = Preset(
        name="test",
        description="Test preset",
        mode="fast"
    )
    assert preset.name == "test"
    assert preset.description == "Test preset"
    assert preset.mode == "fast"
    assert preset.report_format is None
    assert preset.template is None
    assert preset.include_sections is None
    assert preset.exclude_sections is None
    assert preset.verbosity is None


def test_preset_in_builtin_dict():
    """Test that all presets are in BUILTIN_PRESETS dictionary."""
    for preset_name in ["quick", "standard", "audit", "enterprise"]:
        assert preset_name in BUILTIN_PRESETS
        assert isinstance(BUILTIN_PRESETS[preset_name], Preset)


def test_preset_consistency():
    """Test that presets maintain consistency between name and dict key."""
    for key, preset in BUILTIN_PRESETS.items():
        assert key == preset.name