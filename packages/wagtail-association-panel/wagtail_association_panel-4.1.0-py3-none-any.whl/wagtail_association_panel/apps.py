from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailAssociationPanelConfig(AppConfig):
    # noinspection SpellCheckingInspection
    name = 'wagtail_association_panel'
    # noinspection SpellCheckingInspection
    label = 'wagtail_association_panel'
    verbose_name = _("Wagtail Association Panel")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        pass


def get_app_label():
    return WagtailAssociationPanelConfig.label


def reverse_app_url(identifier):
    return reverse(f'{WagtailAssociationPanelConfig.label}:{identifier}')
