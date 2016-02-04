from django.db import models
from apreciacoes.base import ExcecaoDeDominio

class Valor(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Reconhecimento(models.Model):
	reconhecedor = models.ForeignKey('seguranca.Colaborador', related_name='reconhecedor')
	reconhecido = models.ForeignKey('seguranca.Colaborador', related_name='reconhecido')
	valor = models.ForeignKey(Valor)
	justificativa = models.CharField(max_length=200)
	data = models.DateField(auto_now_add=True)

	def alterar_justificativa(self, nova_justificativa, reconhecedor):
		if self.reconhecedor != reconhecedor:
			raise ExcecaoDeDominio('O reconhecimento só pode ser alterado por quem o elaborou')

		self.justificativa = nova_justificativa
