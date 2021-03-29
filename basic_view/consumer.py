import json
from channels.generic.websocket import WebsocketConsumer

import logging

from basic_view import models

log = logging.getLogger(__name__)


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, data):
        text_data_json = json.loads(data)
        try:
            user_id = text_data_json["user_id"]
            try:
                obj = models.UserData.objects.filter(user_id=user_id)
                obj.update(**data)

            except  models.UserData.DoesNotExist:
                pass

            self.send(text_data=json.dumps(text_data_json))
        except Exception as exc:
            log.error("Invalid text received")

    def send(self, text_data=None, bytes_data=None, close=False):
        self.send(text_data=text_data)