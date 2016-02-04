from django.conf.urls import include, url
from seguranca import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
]
