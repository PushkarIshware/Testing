# mysite/routing.py
from channels.auth import AuthMiddlewareStack           # maintain session & authontication
from channels.routing import ProtocolTypeRouter, URLRouter  # node selection (receiver)
import chat.routing
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})