import factory
from reconhecimentos.models import Colaborador
from reconhecimentos.models import Reconhecimento
from reconhecimentos.models import Valor
from datetime import datetime, timedelta
import random

class ColaboradorFactory(factory.django.DjangoModelFactory):
	class Meta:
		model = Colaborador
		django_get_or_create = ('username',)

	username = "Alberto José Roberto"
	password = factory.PostGenerationMethodCall('set_password', 'password')

class ValorFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Valor

	nome = "transparência"

class ReconhecimentoFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Reconhecimento

	reconhecedor = factory.SubFactory(ColaboradorFactory)
	reconhecido = factory.SubFactory(ColaboradorFactory)
	valor = factory.SubFactory(ValorFactory)
	justificativa = "uma justificativa qualquer"
	data = '2015-01-01'
