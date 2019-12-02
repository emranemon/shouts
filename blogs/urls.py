from django.contrib import admin

from django.urls import path, include
from blogs import views

urlpatterns = [
    path('', views.ListBlog.as_view(), name='blogs'),
    path('detail/<int:pk>', views.DetailBlog.as_view(), name='blog_detail'),
    path('create', views.CreatePost.as_view(), name='blog_create'),
    path('update/<int:pk>', views.EditPost.as_view(), name='blog_update'),
    path('delete/<int:pk>', views.DeletePost.as_view(), name='blog_delete'),
    path('edit-comment/<int:pk>', views.EditComment.as_view(), name='comment_edit'),
    path('delete-comment/<int:pk>', views.DeleteComment.as_view(), name='comment_delete'),
    
]