import pytest
from django.urls import reverse

from locnus import forms

pytestmark = [pytest.mark.smoke, pytest.mark.django_db]


def test_post_status_got_called(mocker, account):
    toot = mocker.patch("locnus.models.Mastodon.toot")
    account.toot("Hello, world!")
    toot.assert_called_with("Hello, world!")


def test_toot_form_valid_content(mocker, account):
    toot = mocker.patch("locnus.models.Mastodon.toot")
    form = forms.TootForm({"content": "Hello, world!"})
    assert form.is_valid()
    content = form.cleaned_data["content"]
    account.toot(content)
    toot.assert_called_with("Hello, world!")


def test_get_toot_view(client):
    url = reverse("locnus:get-create-toot")
    response = client.get(url)
    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.skip()
def test_post_toot_view(client, mocker, account):
    toot = mocker.patch("locnus.models.Mastodon.toot")
    url = reverse("locnus:post-create-toot")
    response = client.post(url, data={"content": "Hello, world!"})
    assert response.status_code == 302
    assert response.url == reverse("locnus:home")
    toot.assert_called_with("Hello, world!")
