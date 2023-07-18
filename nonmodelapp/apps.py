from django.apps import AppConfig


class NonmodelappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nonmodelapp'
