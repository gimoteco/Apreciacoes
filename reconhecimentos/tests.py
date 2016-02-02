from django.test import TestCase
from django.core.urlresolvers import reverse
from seguranca.models import Colaborador

class TestesDeViews(TestCase):

    def testa_autenticacao_correta(self):
        dados_da_requisicao = {'cpf': '00000000000', 'data-de-nascimento': '1991-03-16' }
        Colaborador.objects.create(cpf=dados_da_requisicao['cpf'], data_de_nascimento=dados_da_requisicao['data-de-nascimento'])

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertEqual(302, resposta.status_code)

    def testa_autenticacao_incorreta(self):
        dados_da_requisicao = {'cpf': '66666666666', 'data-de-nascimento': '1991-03-16' }

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertEqual(401, resposta.status_code)
