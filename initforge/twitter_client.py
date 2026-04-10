import tweepy

from .utils import load_config


class TwitterClient:
    """Manages Twitter API connection.

    Attributes:
        api: The Tweepy API instance.
        client: The Tweepy Client instance.
    """

    def __init__(self, config: dict = None):
        """Initialize Twitter client.

        Args:
            config: The twitter section of the configuration dictionary.
                    If None, loads from config.json automatically.
        """
        config = config or load_config()["twitter"]
        self.api, self.client = self._setup(config)

    def _setup(self, config: dict) -> tuple[tweepy.API, tweepy.Client]:
        """Set up Tweepy API and Client instances.

        Args:
            config: The twitter section of the configuration dictionary.

        Returns:
            tuple: A tuple containing the Tweepy API and Client instances.
        """
        auth = tweepy.OAuthHandler(
            config["consumer_key"],
            config["consumer_secret"]
        )
        auth.set_access_token(
            config["access_token"],
            config["access_token_secret"]
        )

        api = tweepy.API(auth)
        client = tweepy.Client(
            consumer_key=config["consumer_key"],
            consumer_secret=config["consumer_secret"],
            access_token=config["access_token"],
            access_token_secret=config["access_token_secret"]
        )

        return api, client
