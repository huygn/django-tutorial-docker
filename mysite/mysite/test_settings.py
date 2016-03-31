"""
For Unit test.
    - usage: DJANGO_SETTINGS_MODULE="mysite.test_settings"
"""

from .settings import *


# use dummy cache (equal to disable cache without removing cache methods)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
