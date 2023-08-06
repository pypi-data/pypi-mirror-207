import pytest
from django.urls import reverse

from locnus import views


def test_get_create_server(client):
    url = reverse("locnus:get-create-server")
    response = client.get(url)
    assert response.status_code == 200
    assert "form" in response.context
    assert isinstance(response.context["form"], views.ServerForm)


@pytest.mark.django_db
def test_post_create_server(client):
    url = reverse("locnus:post-create-server")
    response = client.post(url, data={"api_base_url": "https://example-foo.com"})
    assert response.status_code == 302
    assert response.url == reverse("locnus:server-list")
    assert len(views.Server.objects.all()) == 1


@pytest.mark.django_db
def test_get_public_timeline_missing_server(client):
    non_existent_server_pk = 999
    url = reverse("locnus:public-timeline", args=[non_existent_server_pk])
    response = client.get(url)
    assert response.status_code == 404


def get_view_names():
    view_names = ["locnus:server-list", "locnus:get-create-server", "locnus:get-create-account"]
    yield from view_names


@pytest.fixture(params=get_view_names(), ids=str)
def view_name(request):
    return request.param


@pytest.fixture(params=[200])
def response_status_code(request):
    return request.param


@pytest.mark.django_db
def test_get_views(client, view_name, response_status_code):
    url = reverse(view_name)
    r = client.get(url)
    assert r.status_code == response_status_code


@pytest.mark.django_db
def test_get_home_toots_from_db(client, home_toots):
    url = reverse("locnus:home")
    response = client.get(url)
    assert response.status_code == 200
    assert "toots" in response.context


@pytest.mark.django_db
def test_new_toot_in_home_timeline(client, account, home_toots, new_toot_data):
    url = reverse("locnus:home")
    response = client.get(url)

    # make sure the already saved home_toots are in the context
    assert response.context["toots"][0].content == home_toots[0].content

    # save a new toot
    account.add_toot_to_home_timeline(new_toot_data)

    # get the home page again via xmlhttprequest (ajax)
    response = client.get(url, **{"HTTP_HX_REQUEST": "true"})
    content = response.content.decode("utf-8")
    assert str(new_toot_data["id"]) in content


@pytest.mark.django_db
def test_delete_server_from_list(client, server):
    # make sure server is in response context before deleting
    url = reverse("locnus:server-list")
    response = client.get(url)
    assert server in response.context["servers"]

    # delete server
    url = reverse("locnus:delete-server", args=[server.pk])
    client.delete(url)

    # make sure server is not in response context after deleting
    url = reverse("locnus:server-list")
    response = client.get(url)
    assert server not in response.context["servers"]
