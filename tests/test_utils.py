import importlib
import os
import pytest
import initforge.utils as utils_module


@pytest.fixture(autouse=True)
def reset_cache():
    """Reset the global cache before each test."""
    utils_module._project_root = None
    yield
    utils_module._project_root = None


def test_find_project_root_returns_string():
    """Test that find_project_root returns a string."""
    root = utils_module.find_project_root()
    assert isinstance(root, str)


def test_find_project_root_contains_marker():
    """Test that root contains at least one ROOT_MARKER."""
    root = utils_module.find_project_root()
    markers_found = [m for m in utils_module.ROOT_MARKERS if os.path.exists(os.path.join(root, m))]
    assert len(markers_found) > 0


def test_find_project_root_is_cached():
    """Test that second call returns cached value without re-traversal."""
    root1 = utils_module.find_project_root()
    utils_module._project_root = "/fake/cached/path"
    root2 = utils_module.find_project_root()
    assert root2 == "/fake/cached/path"


def test_find_project_root_not_found(tmp_path, monkeypatch):
    """Test that FileNotFoundError is raised when no marker is found."""
    utils_module._project_root = None
    monkeypatch.setattr(utils_module.os.path, "abspath", lambda _: str(tmp_path / "deep" / "nested"))
    with pytest.raises(FileNotFoundError):
        utils_module.find_project_root()


def test_load_config_returns_dict(tmp_path, monkeypatch):
    """Test that load_config returns a dict from config.json."""
    import json
    config_data = {"key": "value"}
    (tmp_path / "config.json").write_text(json.dumps(config_data))
    utils_module._project_root = str(tmp_path)
    result = utils_module.load_config()
    assert result == config_data


def test_load_config_missing_file(tmp_path):
    """Test that load_config raises FileNotFoundError when config.json is missing."""
    utils_module._project_root = str(tmp_path)
    with pytest.raises(FileNotFoundError):
        utils_module.load_config()
