from django.urls import path
from .views import chat_view

urlpatterns = [
    # path('', chat_view, name='chat'),
    path('<str:username>/', chat_view, name='chat'),
]