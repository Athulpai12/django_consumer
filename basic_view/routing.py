from django.urls import re_path

from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/user/(?P<user_id>\w+)/$', consumer.ChatConsumer.as_asgi()),
]