from django.urls import path
from . import views

urlpatterns =[
    path('',  views.home, name = "home_entrans"),
    path('add',views.add, name ="add")
]