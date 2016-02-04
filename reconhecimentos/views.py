from django.shortcuts import render
from django.shortcuts import redirect
from reconhecimentos.models import Reconhecimento
from reconhecimentos.models import Colaborador
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from apreciacoes.base import acesso_anonimo

def pagina_inicial(requisicao):
    reconhecimentos = Reconhecimento.objects.all()
    return render(requisicao, 'pagina_inicial.html', {'reconhecimentos': reconhecimentos})

def perfil(requisicao, id):
    colaborador = Colaborador.objects.get(pk=id)
    return render(requisicao, 'perfil.html', {'colaborador': colaborador})

@acesso_anonimo
def login(requisicao):
    if requisicao.method == "POST":

        cpf = requisicao.POST['cpf']
        data_de_nascimento = requisicao.POST['data-de-nascimento']
        usuario_autenticado = authenticate(cpf=cpf, data_de_nascimento=data_de_nascimento)

        if usuario_autenticado:
            auth_login(requisicao, usuario_autenticado)
            return redirect('pagina_inicial')
        else:
            return HttpResponse('Acesso não autorizado', status=401)

    return render(requisicao, 'login.html')
