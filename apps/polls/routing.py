"""
Channels routing
https://channels.readthedocs.org/en/latest/getting-started.html#routing
"""

from channels.routing import route
from . import consumers


channel_routing = [
    route("websocket.connect", consumers.ws_connect),
    route("websocket.receive", consumers.ws_message),
    route("websocket.disconnect", consumers.ws_disconnect),
]
