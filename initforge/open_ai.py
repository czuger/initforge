import openai

from .utils import load_config


class OpenAIClient:
    """Manages OpenAI API key setup.

    Attributes:
        api_key: The OpenAI API key.
    """

    def __init__(self, config: dict = None, test: bool = False):
        """Initialize OpenAI client.

        Args:
            config: The open_ai section of the configuration dictionary.
                    If None, loads from config.json automatically.
            test: If True, skips API key setup.
        """
        config = config or load_config()["open_ai"]
        self.api_key = self._setup(config, test)

    @staticmethod
    def _setup(config: dict, test: bool) -> str | None:
        """Set up the OpenAI API key.

        Args:
            config: The open_ai section of the configuration dictionary.
            test: If True, skips API key setup.

        Returns:
            str | None: The API key, or None if test mode.
        """
        if test:
            return None

        openai.api_key = config["openai_key"]
        return config["openai_key"]
