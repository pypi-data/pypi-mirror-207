# -*- coding: utf-8 -*-

import sys
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS
from django.urls import reverse
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


def is_running_without_database():
    engine = settings.DATABASES[DEFAULT_DB_ALIAS]['ENGINE']
    return engine == 'django.db.backends.dummy'


class VectorGraphicsConfig(AppConfig):
    name = 'vector_graphics'
    label = 'vector_graphics'
    verbose_name = _("Vector Graphics")
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        if is_running_without_database() or "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        from .models import VectorGraphic
        VectorGraphic.register_storage_signal_handlers()

        # from django.contrib.contenttypes.models import ContentType

        # VectorGraphic.get_template_chooser_config().set_include_content_types_filter(
        #    [ContentType.objects.get_for_model(VectorGraphic).pk])

        from django.contrib.contenttypes.models import ContentType
        from django.db.models import ForeignKey

        from wagtail.admin.forms.models import register_form_field_override
        from wagtail_content_admin.widgets import AdminContentChooser

        register_form_field_override(
            ForeignKey, to=VectorGraphic,
            override={"widget": AdminContentChooser(
                'media_catalogue:chooser',
                max_num_choices=1,
                content_type_filter=([ContentType.objects.get_for_model(VectorGraphic).pk], True))
            }
        )


def get_app_label():
    return VectorGraphicsConfig.label


def reverse_app_url(identifier):
    return reverse(f'{VectorGraphicsConfig.label}:{identifier}')

