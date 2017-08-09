from django.conf.urls import url
from . import views

app_name = "login_register"

urlpatterns = [
	url(r'^$',views.index, name="index")
]