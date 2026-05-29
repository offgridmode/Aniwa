import pytest
import yaml
from aniwa.config_loader import get_flattened_config

def test_load_yaml_config(tmp_path):
    d = tmp_path / "aniwa.yaml"
    content = {
        "mode": "fast",
        "report": {"format": "json", "template": "dark"},
        "sections": {"include": ["summary", "schema"]}
    }
    d.write_text(yaml.dump(content))
    
    config = get_flattened_config(str(d))
    
    assert config["mode"] == "fast"
    assert config["report"] == "json"
    assert config["include"] == "summary,schema"

def test_config_validation_error(tmp_path):
    d = tmp_path / "aniwa.yaml"
    content = {"mode": "invalid_mode"}
    d.write_text(yaml.dump(content))
    
    with pytest.raises(ValueError, match="Invalid mode"):
        get_flattened_config(str(d))

def test_missing_config_returns_empty():
    config = get_flattened_config("non_existent_file.yaml")
    assert config == {}