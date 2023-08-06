from django.core.management import BaseCommand

from locnus.models import Server


class Command(BaseCommand):
    help = "Import a list of server URLs from a text file"

    def add_arguments(self, parser):
        parser.add_argument("path_to_server_urls", type=str)

    def handle(self, *args, **options):
        path_to_server_urls = options["path_to_server_urls"]
        with open(path_to_server_urls) as f:
            server_urls = f.read().splitlines()
        for server_url in server_urls:
            server = Server(api_base_url=server_url)
            server.save()
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {server}"))
