from django.test import TestCase
from reconhecimentos.factories import ColaboradorFactory
from reconhecimentos.factories import ValorFactory
from apreciacoes.base import ExcecaoDeDominio
from django.core.urlresolvers import reverse

class TestesDeViews(TestCase):

    def logar(self, colaborador):
        dados_da_requisicao = {'cpf': colaborador.cpf, 'data-de-nascimento': colaborador.data_de_nascimento.strftime('%d/%m/%Y') }
        resposta = self.client.post(reverse('login'), dados_da_requisicao)

    def testa_logout(self):
        colaborador = ColaboradorFactory()
        self.logar(colaborador)

        resposta = self.client.get(reverse('logout'))
        self.assertRedirects(resposta, reverse('login'))

        resposta = self.client.post(reverse('reconhecer'))
        self.assertEqual(401, resposta.status_code)

    def testa_autenticacao_correta(self):
        colaborador = ColaboradorFactory()
        dados_da_requisicao = {'cpf': colaborador.cpf, 'data-de-nascimento': colaborador.data_de_nascimento.strftime('%d/%m/%Y') }

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertRedirects(resposta, reverse('pagina_inicial'))

    def testa_autenticacao_incorreta(self):
        dados_da_requisicao = {'cpf': '66666666666', 'data-de-nascimento': '16/03/1991' }

        resposta = self.client.post(reverse('login'), dados_da_requisicao)

        self.assertEqual(401, resposta.status_code)

    def testa_o_reconhecimento(self):
        reconhecido = ColaboradorFactory()
        reconhecedor = ColaboradorFactory()
        self.logar(reconhecedor)
        valor = ValorFactory()
        justificativa = 'voce é muito bom'
        dados_da_requisicao = {'valor': valor.id, 'reconhecido': reconhecido.id, 'justificativa': justificativa}

        resposta = self.client.post(reverse('reconhecer'), dados_da_requisicao)

        reconhecimento = reconhecido.reconhecido.all().first()
        self.assertEqual(justificativa, reconhecimento.justificativa)
        self.assertEqual(valor, reconhecimento.valor)
        self.assertEqual(reconhecedor, reconhecimento.reconhecedor)

class TesteDeReconhecimento(TestCase):

    def setUp(self):
        self.reconhecido = ColaboradorFactory()
        self.reconhecedor = ColaboradorFactory()
        self.valor = ValorFactory()
        self.justificativa = "Foi legal aquilo que você fez!"

    def testa_o_reconhecimento_de_uma_habilidade(self):
        self.reconhecido.reconhecer(self.reconhecedor, self.valor, self.justificativa);

        reconhecimento = self.reconhecido.reconhecimentos().first()

        self.assertEqual(1, self.reconhecido.reconhecimentos().count())
        self.assertEqual(self.reconhecedor, reconhecimento.reconhecedor)
        self.assertEqual(self.valor, reconhecimento.valor)
        self.assertEqual(self.justificativa, reconhecimento.justificativa)
