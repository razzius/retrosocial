import django

import channels.layers
from asgiref.sync import async_to_sync


django.setup()

channel_layer = channels.layers.get_channel_layer()

async_to_sync(channel_layer.send)('default', {'type': 'hello'})
