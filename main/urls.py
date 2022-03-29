from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', manga_list, name='manga-list'),
]

