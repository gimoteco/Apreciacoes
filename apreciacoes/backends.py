from seguranca.models import Colaborador

class AutenticadorDeColaborador:

	def authenticate(self, cpf, data_de_nascimento):
		try:
			return Colaborador.objects.get(cpf=cpf, data_de_nascimento=data_de_nascimento)
		except Colaborador.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return Colaborador.objects.get(pk=user_id)
		except Colaborador.DoesNotExist:
			return None
