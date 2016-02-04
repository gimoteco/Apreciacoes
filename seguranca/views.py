from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from apreciacoes.base import acesso_anonimo

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
