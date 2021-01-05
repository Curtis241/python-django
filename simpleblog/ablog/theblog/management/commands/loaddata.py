from django.core.management.base import BaseCommand, CommandError
import os
from django.apps import apps
from django.conf import settings


class Command(BaseCommand):
    help = 'Loads initial data'

    def __init__(self):
        super().__init__()
        os.environ['DJANGO_SETTINGS_MODULE'] = 'ablog.settings'
        apps.populate(settings.INSTALLED_APPS)

    def handle(self, *args, **options):
        for model in apps.get_models():
            if hasattr(model, "load_data"):
                if model().load_data():
                    print(f"Added {model.__name__} rows")
                else:
                    print(f"Skipped adding {model.__name__} rows")
        self.stdout.write(self.style.SUCCESS("Loaded initial data"))