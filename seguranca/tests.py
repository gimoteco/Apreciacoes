from django.test import TestCase
from django.core.urlresolvers import reverse
from seguranca.models import Colaborador
from seguranca.factories import ColaboradorFactory

class TestesDeViews(TestCase):

    def testa_autenticacao_correta(self):
        colaborador = ColaboradorFactory()
        dados_da_requisicao = {'cpf': colaborador.cpf, 'data-de-nascimento': colaborador.data_de_nascimento.date() }

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertRedirects(resposta, reverse('pagina_inicial'))

    def testa_autenticacao_incorreta(self):
        dados_da_requisicao = {'cpf': '66666666666', 'data-de-nascimento': '1991-03-16' }

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertEqual(401, resposta.status_code)
