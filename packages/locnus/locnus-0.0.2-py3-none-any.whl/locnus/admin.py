from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Account, Client, Server, Status, Timeline


@admin.register(Client)
class ClientModelAdmin(ModelAdmin):
    list_display = ("server", "name")
    fields = ("name", "remote_id", "secret")


@admin.register(Server)
class ServerModelAdmin(ModelAdmin):
    list_display = ("api_base_url",)
    fields = ("api_base_url", "client")


@admin.register(Account)
class AccountModelAdmin(ModelAdmin):
    list_display = ("server", "username")
    fields = ("server", "username", "access_token")


@admin.register(Status)
class StatusModelAdmin(ModelAdmin):
    list_display = ("id", "created_at")
    readonly_fields = ("created_at",)
    fields = ("id", "created_at", "data")


@admin.register(Timeline)
class TimelineModelAdmin(ModelAdmin):
    list_display = ("id", "tag", "account", "server")
    fields = ("tag", "account", "server", "status")
