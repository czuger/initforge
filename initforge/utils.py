import json
import logging
import os

ROOT_MARKERS = {'requirements.txt', '.git', 'README.md', 'pyproject.toml'}

logger = logging.getLogger(__name__)

_project_root: str | None = None


def find_project_root() -> str:
    """Find project root by traversing up until a root marker is found.

    Caches the result in a global variable to avoid re-reading at each call.

    Returns:
        str: Absolute path to project root.

    Raises:
        FileNotFoundError: If project root cannot be found.
    """
    global _project_root

    if _project_root is not None:
        return _project_root

    # Start from the current working directory (the project using this library)
    # rather than __file__ which points to the library's own location
    current = os.path.abspath(os.getcwd())

    while current != os.path.dirname(current):
        if any(os.path.exists(os.path.join(current, marker)) for marker in ROOT_MARKERS):
            _project_root = current
            return _project_root
        current = os.path.dirname(current)

    raise FileNotFoundError("Project root not found")


def load_config() -> dict:
    """Load configuration from config.json at project root.

    Returns:
        dict: Configuration data.
    """
    config_path = os.path.join(find_project_root(), 'config.json')

    with open(config_path, 'r') as config_file:
        return json.load(config_file)
