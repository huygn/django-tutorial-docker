"""
Configurations for local development.
"""
import os

from django.conf import settings


def show_toolbar(request):
    """
    For showing django-debug-toolbar when running inside docker, for detail:
    https://github.com/gnhuy91/til/blob/master/django/debug-toolbar-in-docker.md
    """
    if request.is_ajax():
        return False

    return bool(settings.DEBUG)
