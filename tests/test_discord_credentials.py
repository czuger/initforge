import pytest

from initforge.discord_credentials import DiscordOminAuthCredentials


def test_from_config_with_explicit_config():
    """Build credentials from an explicit config dictionary."""
    config = {
        "discord": {
            "omin_auth": {
                "client_id": "cid",
                "client_secret": "csecret",
                "redirect_uri": "https://example.com/callback"
            }
        }
    }

    credentials = DiscordOminAuthCredentials.from_config(config)

    assert credentials.client_id == "cid"
    assert credentials.client_secret == "csecret"
    assert credentials.redirect_uri == "https://example.com/callback"


def test_from_config_missing_key_raises_key_error():
    """Raise KeyError when required key is missing."""
    config = {
        "discord": {
            "omin_auth": {
                "client_id": "cid",
                "redirect_uri": "https://example.com/callback"
            }
        }
    }

    with pytest.raises(KeyError):
        DiscordOminAuthCredentials.from_config(config)


def test_as_dict_returns_expected_payload():
    """Return a plain dictionary with all fields."""
    credentials = DiscordOminAuthCredentials(
        client_id="cid",
        client_secret="csecret",
        redirect_uri="https://example.com/callback"
    )

    assert credentials.as_dict() == {
        "client_id": "cid",
        "client_secret": "csecret",
        "redirect_uri": "https://example.com/callback"
    }
