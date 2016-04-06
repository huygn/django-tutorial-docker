import json

from channels import Group
from channels.sessions import channel_session, enforce_ordering
from channels.auth import channel_session_user_from_http


@enforce_ordering(slight=True)
@channel_session_user_from_http
def ws_connect(message):
    Group('tasks').add(message.reply_channel)
    Group('tasks').send({'text': json.dumps('client connected')})


@enforce_ordering(slight=True)
@channel_session
def ws_message(message):
    msg = message.content['text']
    Group('tasks').send({'text': json.dumps(
        'AGSI: received msg: {} from WebSocket client!'.format(msg))})


@enforce_ordering(slight=True)
@channel_session
def ws_disconnect(message):
    Group('tasks').discard(message.reply_channel)
