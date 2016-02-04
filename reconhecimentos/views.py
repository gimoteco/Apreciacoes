from django.shortcuts import render
from reconhecimentos.models import Reconhecimento

def pagina_inicial(requisicao):
    reconhecimentos = Reconhecimento.objects.all()
    return render(requisicao, 'pagina_inicial.html', {'reconhecimentos': reconhecimentos})
