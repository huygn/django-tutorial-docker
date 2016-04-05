from __future__ import absolute_import

from time import sleep

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task(bind=True)
def long_task(self, i):
    print('request id: {}'.format(self.request.id))
    sleep(i)
    print('slept {} seconds!'.format(i))
    return True


@shared_task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
