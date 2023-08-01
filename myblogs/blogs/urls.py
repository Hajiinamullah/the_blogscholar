from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('createblog/', views.create_blog, name='create_blog'),
    path('blogg/', views.blogg, name='blogg'),
    path('comment_form/<int:blog_id>/', views.comment_form, name='comment_form'),
    path('blog_detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('comment_submit/<int:blog_id>/', views.comment_submit, name='comment_submit'),
    path('blog_list', views.blog_list, name='blog_list'),
]
