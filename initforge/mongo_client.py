from mongoengine import connect

from .utils import load_config


class MongoClient:
    """Manages MongoDB connection.

    Attributes:
        db_name: The name of the connected database.
    """

    def __init__(self, config: dict = None, test: bool = False):
        """Initialize MongoDB connection.

        Args:
            config: The mongo section of the configuration dictionary.
                    If None, loads from config.json automatically.
            test: If True, uses a test database.
        """
        config = config or load_config()["mongo"]
        self.db_name = self._setup(config, test)

    @staticmethod
    def _setup(config: dict, test: bool) -> str:
        """Connect to the MongoDB database.

        Args:
            config: The mongo section of the configuration dictionary.
            test: If True, uses a test database.

        Returns:
            str: The name of the connected database.
        """
        db_name = f"{config['database']}_test" if test else config["database"]

        connect(
            db=db_name,
            host=config["server"],
            username=config["user"],
            password=config["pass"]
        )

        return db_name
