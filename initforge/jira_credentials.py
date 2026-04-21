from dataclasses import dataclass

from .utils import load_config


@dataclass(frozen=True)
class JiraCredentials:
    """Stores Jira API access information."""

    host: str
    email: str
    api_token: str

    @classmethod
    def from_config(cls, config: dict = None) -> "JiraCredentials":
        """Build Jira credentials from configuration data."""

        source = config or load_config()
        jira_section = source["jira"]
        return cls(
            host=jira_section["host"],
            email=jira_section["email"],
            api_token=jira_section["api_token"],
        )

    def as_dict(self) -> dict:
        """Expose Jira credentials as plain dict."""

        return {
            "host": self.host,
            "email": self.email,
            "api_token": self.api_token,
        }
