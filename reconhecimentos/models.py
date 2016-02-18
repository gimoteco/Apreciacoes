from django.db import models
from apreciacoes.base import ExcecaoDeDominio
from django.contrib.auth.models import AbstractBaseUser

class Colaborador(AbstractBaseUser):
	cpf = models.CharField(max_length=11, unique=True)
	nome = models.CharField(max_length=200)
	data_de_nascimento = models.DateField()

	USERNAME_FIELD = 'cpf'

	def reconhecer(self, reconhecedor, valor, justificativa):
		if not justificativa.strip():
			raise ExcecaoDeDominio('A sua justificativa deve ser informada')

		self.reconhecido.create(reconhecedor=reconhecedor, valor=valor, justificativa=justificativa)

	def reconhecimentos(self):
		return self.reconhecido.all()

	def __str__(self):
		return self.nome

class Valor(models.Model):
	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Reconhecimento(models.Model):
	reconhecedor = models.ForeignKey(Colaborador, related_name='reconhecedor')
	reconhecido = models.ForeignKey(Colaborador, related_name='reconhecido')
	valor = models.ForeignKey(Valor)
	justificativa = models.CharField(max_length=200)
	data = models.DateField(auto_now_add=True)

	def alterar_justificativa(self, nova_justificativa, reconhecedor):
		if self.reconhecedor != reconhecedor:
			raise ExcecaoDeDominio('O reconhecimento só pode ser alterado por quem o elaborou')

		self.justificativa = nova_justificativa
