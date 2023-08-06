from unittest.mock import patch

from locnus import models


def test_from_api_base_url(mocker):
    mocker.patch("locnus.models.Mastodon.create_app", return_value=("remote_id", "secret"))
    client = models.Client.from_api_base_url("https://example.com", name="mocked_client")
    assert client.name == "mocked_client"
    assert client.remote_id == "remote_id"
    assert client.secret == "secret"


def test_from_api_base_url_correct_create_app_params(mocker):
    create_app = mocker.patch("locnus.models.Mastodon.create_app", return_value=("remote_id", "secret"))
    models.Client.from_api_base_url("https://example.com", name="mocked_client")
    create_app.assert_called_with("mocked_client", api_base_url="https://example.com")


@patch("locnus.models.Mastodon.create_app", return_value=("remote_id", "secret"))
def test_from_api_base_url_unittest(mock1):
    client = models.Client.from_api_base_url("https://example.com", name="mocked_client")
    assert client.name == "mocked_client"
    assert client.remote_id == "remote_id"
    assert client.secret == "secret"


def test_from_api_base_url_context_manager():
    with patch("locnus.models.Mastodon.create_app", return_value=("remote_id", "secret")):
        client = models.Client.from_api_base_url("https://example.com", name="mocked_client")
    assert client.name == "mocked_client"
    assert client.remote_id == "remote_id"
    assert client.secret == "secret"
