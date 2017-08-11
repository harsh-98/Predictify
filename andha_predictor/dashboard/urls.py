from django.conf.urls import url
from . import views

app_name = "dashboard"

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^logoutUser$', views.logoutUser, name="logoutUser"),
	url(r'^predictScore$', views.predictScore, name="predictScore"),
]