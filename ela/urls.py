from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('image/' , index , name="index" ),
    path('',index,name="index"),
]