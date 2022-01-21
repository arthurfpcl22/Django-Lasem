from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path 
from S_Lasem import consumer1

websocket_urlPattern=[
	path('ws/teste/',consumer1.DashConsumer),
]

application=ProtocolTypeRouter({
	# (http->django views is added by default)
	'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))

	

})
