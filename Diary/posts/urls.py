from django.urls import path
from . import views
urlpatterns = [
    #path('',view.index),
    path('posts/', views.post_list, name='post-list'), #name속성을 주면 나중에 하나하나 수정안해도 되고 유지보수에 좋음.
    path('posts/new', views.post_create, name='post-create'),
    path('posts/<int:post_id>', views.post_detail, name='post-detail'),
    #path('posts/<int:post_id>/edit', views.post_update),
    #path('posts/<int:post_id>/delete', views.post_delet),
]
