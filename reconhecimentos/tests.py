from django.test import TestCase
from seguranca.factories import ColaboradorFactory
from reconhecimentos.factories import ValorFactory
from apreciacoes.base import ExcecaoDeDominio

class TesteDeReconhecimento(TestCase):

    def setUp(self):
        self.reconhecido = ColaboradorFactory()
        self.reconhecedor = ColaboradorFactory()
        self.valor = ValorFactory()
        self.justificativa = "Foi legal aquilo que você fez!"

    def testa_o_reconhecimento_de_uma_habilidade(self):
        self.reconhecido.reconhecer(self.reconhecedor, self.valor, self.justificativa);

        reconhecimento = self.reconhecido.reconhecimentos()[0]
        self.assertEqual(1, len(self.reconhecido.reconhecimentos_por_valor(self.valor)))
        self.assertEqual(self.reconhecedor, reconhecimento.reconhecedor)
        self.assertEqual(self.valor, reconhecimento.valor)
        self.assertEqual(self.justificativa, reconhecimento.justificativa)

    def testa_que_o_colaborador_nao_pode_se_reconher(self):
        parametros = (self.reconhecido, self.valor, 'Parabéns pela iniciativa')
        mensagem_esperada = 'O colaborador nao pode reconher a si próprio'

        self.assertRaisesMessage(ExcecaoDeDominio, mensagem_esperada, self.reconhecido.reconhecer, *parametros)
