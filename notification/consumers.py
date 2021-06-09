from django.contrib.auth import get_user_model
from django.conf import settings
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

import json

User = get_user_model()

class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        """
        Called when the websocket is handshaking as part of initial connection.
        """
        print("NotificationConsumer: connect: " + str(self.scope["user"]) )
        await self.accept()

    async def disconnect(self, code):
        """
        Called when the WebSocket closes for any reason.
        """
        print("NotificationConsumer: disconnect")

    async def receive_json(self, content):
        """
        Called when we get a text frame. Channels will JSON-decode the payload
        for us and pass it as the first argument.
        """
        command = content.get("command", None)
        print("NotificationConsumer: receive_json. Command: " + command)

    async def display_progress_bar(self, shouldDisplay):
        print("NotificationConsumer: display_progress_bar: " + str(shouldDisplay)) 
        await self.send_json(
			{
				"progress_bar": shouldDisplay,
			},
		)
       