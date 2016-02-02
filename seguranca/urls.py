from django.conf.urls import include, url
from seguranca import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^$', views.pagina_inicial, name="pagina_inicial"),
]
