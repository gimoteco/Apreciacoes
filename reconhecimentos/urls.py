from django.conf.urls import include, url
from reconhecimentos import views

urlpatterns = [
    url(r'^$', views.pagina_inicial, name="pagina_inicial"),
]
