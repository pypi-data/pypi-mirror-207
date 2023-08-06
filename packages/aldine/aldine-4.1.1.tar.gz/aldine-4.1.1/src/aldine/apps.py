from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AldineConfig(AppConfig):
    name = 'aldine'
    label = 'aldine'
    verbose_name = _("Aldine")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):

        from .cells import ResponsiveCell

        pass


def get_app_label():
    return AldineConfig.label


def reverse_app_url(identifier):
    return reverse(f'{AldineConfig.label}:{identifier}')

