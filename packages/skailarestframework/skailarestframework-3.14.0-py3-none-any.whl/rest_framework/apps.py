from skailar.apps import AppConfig


class RestFrameworkConfig(AppConfig):
    name = 'rest_framework'
    verbose_name = "Skailar REST framework"

    def ready(self):
        # Add System checks
        from .checks import pagination_system_check  # NOQA
