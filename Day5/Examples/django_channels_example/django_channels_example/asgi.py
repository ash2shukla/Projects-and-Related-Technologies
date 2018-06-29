from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from dc_app.views import DemoConsumer

asgi_application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': URLRouter([
        path('demo_socket/', DemoConsumer)
        ]),
})
