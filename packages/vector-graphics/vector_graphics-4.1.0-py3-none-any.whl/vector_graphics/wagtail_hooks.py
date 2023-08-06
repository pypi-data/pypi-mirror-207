from django.urls import include, path

from wagtail.core import hooks

from . import admin_urls
from .apps import get_app_label

APP_LABEL = get_app_label()


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path(APP_LABEL + '/', include(admin_urls, namespace=APP_LABEL)),
    ]
