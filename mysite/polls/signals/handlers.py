from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.cache import cache

from polls.models import Question


class QuestionHandlers(object):
    """ below handlers does NOT need (self) argument. """

    @receiver(pre_save, sender=Question)
    def pre_save_handler(sender, **kwargs):
        # print('======== QuestionHandlers: pre_save signal catched!')
        pass

    @receiver(post_save, sender=Question)
    def post_save_handler(sender, **kwargs):
        # print('======== QuestionHandlers: post_save signal catched!')
        # cache.delete('')
        pass
