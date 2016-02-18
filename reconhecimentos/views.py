from datetime import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from reconhecimentos.models import Reconhecimento
from reconhecimentos.models import Colaborador
from reconhecimentos.models import Valor
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from apreciacoes.base import acesso_anonimo

def pagina_inicial(requisicao):
    reconhecimentos = Reconhecimento.objects.all()
    return render(requisicao, 'pagina_inicial.html', {'reconhecimentos': reconhecimentos})

def perfil(requisicao, id):
    colaborador = Colaborador.objects.get(pk=id)
    return render(requisicao, 'perfil.html', {'colaborador': colaborador})

def reconhecer(requisicao):
    if requisicao.method == "POST":
        reconhecido = Colaborador.objects.get(pk=requisicao.POST['reconhecido'])
        justificativa = requisicao.POST['justificativa']
        valor = Valor.objects.get(pk=requisicao.POST['valor'])
        reconhecedor = requisicao.user

        reconhecido.reconhecer(reconhecedor, valor, justificativa)

        return redirect(perfil, reconhecido.id)

    valores = Valor.objects.all()
    colaboradores = Colaborador.objects.all()
    dados = dict(colaboradores=colaboradores, valores=valores)
    return render(requisicao, 'reconhecer.html', dados)

def logout(requisicao):
    auth_logout(requisicao)
    return redirect('login')

@acesso_anonimo
def login(requisicao):
    if requisicao.method == "POST":
        cpf = requisicao.POST['cpf'].replace('.', '').replace('-', '')
        data_de_nascimento = datetime.strptime(requisicao.POST['data-de-nascimento'], '%d/%m/%Y')
        usuario_autenticado = authenticate(cpf=cpf, data_de_nascimento=data_de_nascimento)

        if usuario_autenticado:
            auth_login(requisicao, usuario_autenticado)
            return redirect('pagina_inicial')
        else:
            return HttpResponse('Acesso não autorizado', status=401)

    return render(requisicao, 'login.html')
