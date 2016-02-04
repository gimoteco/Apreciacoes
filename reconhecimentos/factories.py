import factory
from reconhecimentos.models import Colaborador
from reconhecimentos.models import Reconhecimento
from reconhecimentos.models import Valor
from datetime import datetime, timedelta
import random

def gerar_data_aleatoria():
	anos_atras = random.randint(20, 80) * 365
	return datetime.today() - timedelta(days=anos_atras)

class ColaboradorFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Colaborador

	cpf = factory.Sequence(lambda i: str(random.randint(10000000000, 99999999999)))
	nome = "Alberto José Roberto"
	data_de_nascimento = factory.Sequence(lambda i: gerar_data_aleatoria())

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
