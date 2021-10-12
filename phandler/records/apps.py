from django.apps import AppConfig


class RecordsConfig(AppConfig):
    name = "phandler.records"

    def ready(self):
        try:
            import phandler.records.signals  # noqa F401
        except ImportError:
            pass
