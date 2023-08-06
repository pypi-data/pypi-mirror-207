import pytest
from django.db import IntegrityError

from locnus.models import Account, Server, Status, Timeline


@pytest.mark.django_db
def test_server_in_database(mastodon_client):
    server = Server(api_base_url="https://example.com", client=mastodon_client)

    server.save()
    assert server in Server.objects.all()


@pytest.mark.django_db
def test_no_account_without_server():
    account = Account()
    with pytest.raises(IntegrityError):
        account.save()


@pytest.mark.django_db
def test_account_in_database(server, mastodon_client):
    account = Account(server=server, username="alice", access_token="access_token")
    account.save()
    assert server.accounts.count() == 1
    assert len(server.accounts.all()) == 1


@pytest.mark.django_db
def test_modifies_database(mastodon_client):
    server = Server(api_base_url="https://example.com", client=mastodon_client)
    server.save()
    assert server in Server.objects.all()


def test_with_different_settings(settings):
    settings.ADMIN_ENABLED = False
    assert True


@pytest.mark.django_db
def test_create_status(status):
    assert status in Status.objects.all()


@pytest.fixture(params=[Timeline.Tag.PUBLIC, Timeline.Tag.LOCAL])
def timeline_tag(request):
    return request.param


@pytest.fixture(params=[Server.timeline_public, Server.timeline_local])
def get_timeline(request):
    return request.param


@pytest.mark.django_db
def test_tagged_status_in_appropriate_timeline_via_fixture_params(timeline_tag, get_timeline, status, server):
    item = Timeline(status=status, server=server, tag=timeline_tag)
    item.save()
    timeline_qs = get_timeline(server)
    status_pks = {x.status.pk for x in timeline_qs}
    should_be_in_timeline = timeline_tag.name.lower() in str(get_timeline)
    if should_be_in_timeline:
        assert status.pk in status_pks
    else:
        assert status.pk not in status_pks


@pytest.mark.django_db
@pytest.mark.parametrize(
    "tag, get_timeline, should_be_in_timeline",
    [
        (Timeline.Tag.PUBLIC, Server.timeline_public, True),
        (Timeline.Tag.LOCAL, Server.timeline_public, False),
        pytest.param(Timeline.Tag.LOCAL, Server.timeline_local, True, marks=pytest.mark.smoke),
        (Timeline.Tag.PUBLIC, Server.timeline_local, False),
    ],
)
def test_tagged_status_in_appropriate_timeline(tag, get_timeline, should_be_in_timeline, status, server):
    item = Timeline(status=status, server=server, tag=tag)
    item.save()
    timeline_qs = get_timeline(server)
    status_pks = {x.status.pk for x in timeline_qs}
    if should_be_in_timeline:
        assert status.pk in status_pks
    else:
        assert status.pk not in status_pks


@pytest.mark.django_db
def test_add_status_for_home_timeline(status, account):
    item = Timeline(status=status, account=account, server=account.server, tag=Timeline.Tag.HOME)
    item.save()
    home_qs = account.timeline_home()
    status_pks = {x.pk for x in home_qs}
    assert status.pk in status_pks


@pytest.mark.parametrize(
    "first, last",
    [
        # ("Alice", "Alice"),
        ("Alice", "Smith"),
        ("Bob", "Smith"),
        ("Alice", "Jones"),
    ],
)
def test_combinations(first, last):
    assert first != last


@pytest.mark.django_db
@pytest.mark.num_toots(3)
def test_save_a_number_of_toots(db, status):
    assert Status.objects.count() == 3


@pytest.mark.django_db
def test_delete_account(account, home_toots):
    account.delete()
    for toot in home_toots:
        assert toot not in Timeline.objects.filter(account=account)
