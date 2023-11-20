from django.urls import path
from .views import *
urlpatterns = [
    path('', home , name='base'),
    path('post/', post, name='post'),
    path('shop/', shop, name='shop')
]