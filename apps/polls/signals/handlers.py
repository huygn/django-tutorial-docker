import json

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from celery.signals import after_task_publish, task_prerun, task_postrun
from channels import Group

from polls.models import Question, Choice


class QuestionHandlers(object):
    """ below handlers does NOT need (self) argument. """

    @receiver(pre_save, sender=Question)
    def pre_save_handler(sender, **kwargs):
        pass

    @receiver(post_save, sender=Question)
    def post_save_handler(sender, **kwargs):
        pass


class ChoiceHandlers(object):
    """ below handlers does NOT need (self) argument. """

    @receiver(pre_save, sender=Choice)
    def pre_save_handler(sender, **kwargs):
        pass

    @receiver(post_save, sender=Choice)
    def post_save_handler(sender, **kwargs):
        Group("tasks").send({'text': json.dumps(
            'Choice model: post_save signal catched!')})
        pass


class CeleryHandlers(object):
    """
    Signal handlers for Celery tasks
    http://docs.celeryproject.org/en/latest/userguide/signals.html#task-signals
    """

    @after_task_publish.connect
    def task_sent_handler(sender=None, body=None, **kwargs):
        msg = ('Task [{sender}], id [{body[id]}], '
               '{kwargs} has been sent to Broker')
        msg = msg.format(**locals())
        Group('tasks').send({'text': json.dumps(msg)})

    @task_prerun.connect
    def task_prerun_handler(
            task_id, task, *args, **kwargs):
        msg = 'Task name: {task.name}, id: {task_id}, {args}, {kwargs} Started'
        msg = msg.format(**locals())
        print(msg)
        Group('tasks').send({'text': json.dumps(msg)})

    @task_postrun.connect
    def task_postrun_handler(
            task_id, task, state, retval=None, *args, **kwargs):
        msg = ('Task name: {task.name}, id: {task_id}, {retval}, '
               '{state}, {args}, {kwargs[args]} Finished')
        msg = msg.format(**locals())
        print(msg)
        Group('tasks').send({'text': json.dumps(msg)})
