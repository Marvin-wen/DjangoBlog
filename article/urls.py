from django.urls import path
from .views import *


app_name = 'article'

urlpatterns = [
    path('article-list/', article_list, name='article-list'),
    path('article-detail/<int:id>/', article_detail, name='article-detail'),
    path('article-create/', article_create, name='article-create'),
    path('article-delete/<int:id>/', article_delete, name='article-delete'),
    path('article-update/<int:id>/', article_update, name='article-update'),
]
