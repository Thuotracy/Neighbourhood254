from django.apps import AppConfig


class HoodappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = 'hoodapp'

    def ready(self):
        import hoodapp.signals
