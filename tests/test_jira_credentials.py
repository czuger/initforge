import pytest

from initforge.jira_credentials import JiraCredentials


def test_from_config_extracts_values():
    config = {"jira": {"host": "https://jira.example.com", "email": "user@example.com", "api_token": "token"}}

    credentials = JiraCredentials.from_config(config)

    assert credentials.host == "https://jira.example.com"
    assert credentials.email == "user@example.com"
    assert credentials.api_token == "token"


def test_from_config_missing_key_raises_key_error():
    config = {"jira": {"host": "https://jira.example.com", "api_token": "token"}}

    with pytest.raises(KeyError):
        JiraCredentials.from_config(config)


def test_as_dict_matches_fields():
    credentials = JiraCredentials(host="h", email="e", api_token="t")

    assert credentials.as_dict() == {"host": "h", "email": "e", "api_token": "t"}
