import logging
import secrets
import os

from flask import Flask

from .utils import find_project_root, load_config

logger = logging.getLogger(__name__)


class FlaskAppConfiguration:
    """Manages Flask application configuration and service initialization.

    Attributes:
        app: The Flask application instance.
        secret_key: The secret key for the Flask app.
        config: The configuration dictionary.
    """

    def __init__(self, app: Flask = None):
        """Initialize the Flask application configuration.

        Args:
            app: The Flask application instance to configure.
            test: If True, disables OpenAI API key and uses a test database.
        """
        self.app = app
        self.test = test
        self.config = load_config()
        self.secret_key = self._load_secret_key()

    @staticmethod
    def _load_secret_key() -> str:
        """Load secret key from secret_key.txt at project root.

        Logs an error if secret_key.txt does not exist and returns a random
        secret key instead.

        Returns:
            str: Secret key.
        """
        secret_key_path = os.path.join(find_project_root(), 'secret_key.txt')

        try:
            with open(secret_key_path, 'r') as secret_key_file:
                logger.info("Secret key found")
                return secret_key_file.read().strip()

        except FileNotFoundError:
            logger.error("secret_key.txt not found at %s, using random secret key", secret_key_path)
            return secrets.token_hex(32)
