from dataclasses import dataclass

from .utils import load_config


@dataclass(frozen=True)
class DiscordOminAuthCredentials:
    """Stores Discord Omin Auth credentials."""

    client_id: str
    client_secret: str
    redirect_uri: str

    @classmethod
    def from_config(cls, config: dict = None) -> "DiscordOminAuthCredentials":
        """Build credentials from config data.

        Args:
            config: Optional config dictionary.
                    If None, loads from config.json automatically.

        Returns:
            DiscordOminAuthCredentials: Validated credentials object.
        """
        source = config or load_config()
        omin_auth = source["discord"]["omin_auth"]
        return cls(
            client_id=omin_auth["client_id"],
            client_secret=omin_auth["client_secret"],
            redirect_uri=omin_auth["redirect_uri"]
        )

    def as_dict(self) -> dict:
        """Expose credentials as a plain dictionary."""
        return {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri
        }
