from django.urls import path
from . import views

urlpatterns =[
    path('blog_system/',views.home, name = 'home1'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:post_id>/', views.update_post, name='update_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posts/', views.get_posts),
    path('posts/create/', views.create_post_api),
    path('posts/update/<int:id>/', views.update_post_api),
    path('posts/delete/<int:id>/', views.delete_post_api),
]