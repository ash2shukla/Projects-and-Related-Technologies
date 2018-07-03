from channels.generic.websocket import JsonWebsocketConsumer
from time import sleep
# from django.core.cache import cache
from asgiref.sync import async_to_sync
import qrcode
import base64
from io import BytesIO


class DemoConsumer(JsonWebsocketConsumer):
    def qr_to_base64(self, i):
        """
        Creates a base64 string corresponding to some_text's QR
        """
        img_obj = qrcode.make(str(i))
        qr_stream = BytesIO()
        img_obj.save(qr_stream)
        qr_bytes = qr_stream.getvalue()
        print(qr_bytes)
        return base64.b64encode(qr_bytes).decode()

    def connect(self):
        self.accept()

    def receive_json(self, json_data):
        for i in range(10):
            self.send_json({'message': 'data:image/png;base64,' + self.qr_to_base64(i)})
            sleep(1)

    def disconnect(self, close_code):
        print('Here it has disconnected')
        self.send_json({'message': "Goodbye!"})

    def somemethod(self, message):
        print(message) 

