from django.conf.urls import include, url
from reconhecimentos import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^$', views.pagina_inicial, name="pagina_inicial"),
    url(r'^perfil/(\d+)/$', views.perfil, name="perfil"),
    url(r'^reconhecer/$', views.reconhecer, name="reconhecer"),
]
