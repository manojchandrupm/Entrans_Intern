from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.SimpleConsumer.as_asgi()),
]

'''use the below javascript code to check websocket connection enable with django'''
#const ws = new WebSocket('ws://localhost:8000/ws/chat/');

# ws.onopen = () => {
#     console.log('✅ Connected to WebSocket!');
#     ws.send('Hello from client!');
# };

# ws.onmessage = (e) => {
#     console.log('📨 Received:', e.data);
# };

# ws.onerror = (e) => {
#     console.log('❌ Error:', e);
# };

# ws.onclose = () => {
#     console.log('🔌 Disconnected');
# };