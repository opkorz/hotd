from django.conf.urls import url, include
from django.contrib import admin

from heros_api import views

urlpatterns = [
	url(r'^$', views.HotdAPI.as_view(), name='hotd')	
]

