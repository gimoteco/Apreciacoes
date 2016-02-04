import factory
from seguranca.factories import ColaboradorFactory
from reconhecimentos.models import Reconhecimento
from reconhecimentos.models import Valor

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
