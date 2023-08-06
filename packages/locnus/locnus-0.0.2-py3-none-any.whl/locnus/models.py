from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from mastodon import Mastodon


class Client(models.Model):
    name = models.CharField(max_length=100, default="pytooterapp")
    remote_id = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.name}>"

    def set_remote_id_and_secret(self, api_base_url):
        self.remote_id, self.secret = Mastodon.create_app(self.name, api_base_url=api_base_url)

    @classmethod
    def from_api_base_url(cls, api_base_url, name=None):
        client = cls()
        if name is not None:
            client.name = name
        client.set_remote_id_and_secret(api_base_url)
        return client


class Server(models.Model):
    api_base_url = models.URLField(verbose_name="API Base URL", unique=True)
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name="server")

    def __str__(self):
        return self.api_base_url

    def get_access_token(self, username, password):
        if self.client is None:
            self.client = Client.from_api_base_url(self.api_base_url)

        mastodon = Mastodon(
            client_id=self.client.remote_id,
            client_secret=self.client.secret,
            api_base_url=self.api_base_url,
        )
        return mastodon.log_in(username, password)

    def public_timeline(self):
        mastodon = Mastodon(api_base_url=self.api_base_url)
        return mastodon.timeline_public()

    def timeline_public(self):
        return Timeline.objects.public().filter(server=self)

    def timeline_local(self):
        return Timeline.objects.local().filter(server=self)


class Account(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="accounts")
    username = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.username}, {self.server}>"

    def personal_timeline(self):
        mastodon = Mastodon(
            access_token=self.access_token,
            api_base_url=self.server.api_base_url,
        )
        return mastodon.timeline_home()

    def timeline_home(self):
        timeline_qs = Timeline.objects.filter(tag=Timeline.Tag.HOME, account=self)
        toots = [timeline.status for timeline in timeline_qs]
        return toots

    def toot(self, content):
        mastodon = Mastodon(
            access_token=self.access_token,
            api_base_url=self.server.api_base_url,
        )
        response = mastodon.toot(content)
        return response

    def add_toot_to_home_timeline(self, toot):
        status = Status(pk=toot["id"], created_at=toot["created_at"], data=toot)
        status.save()
        item = Timeline(account=self, status=status, tag=Timeline.Tag.HOME, server=self.server)
        item.save()
        return item


class TimelineManager(models.Manager):
    def public(self):
        return self.filter(tag=Timeline.Tag.PUBLIC)

    def local(self):
        return self.filter(tag=Timeline.Tag.LOCAL)


class Timeline(models.Model):
    status = models.ForeignKey("Status", on_delete=models.CASCADE, related_name="timelines")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    objects = TimelineManager()

    class Tag(models.IntegerChoices):
        PUBLIC = 1
        LOCAL = 2
        HOME = 3

    tag = models.IntegerField(choices=Tag.choices)


class Status(models.Model):
    id = models.BigIntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(encoder=DjangoJSONEncoder)
    timeline = models.ManyToManyField(Server, through=Timeline)

    @property
    def content(self):
        return self.data.get("content")

    @property
    def display_name(self):
        return self.data.get("account", {}).get("display_name")
