import pytest
from django.core.management import call_command

from locnus.models import Server


@pytest.fixture()
def path_to_server_urls(tmp_path):
    server_urls = [
        "https://example.com",
        "https://mastodon.social",
        "https://mastodon.online",
    ]
    path = tmp_path / "server_urls.txt"
    path.write_text("\n".join(server_urls))
    return path


@pytest.mark.django_db
def test_import_server(path_to_server_urls):
    call_command("import_server_urls", path_to_server_urls)
    assert Server.objects.count() > 0
    server_urls = [server.api_base_url for server in Server.objects.all()]
    assert "https://mastodon.social" in server_urls
