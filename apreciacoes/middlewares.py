from django.http import HttpResponse
from apreciacoes.base import permite_acesso_anonimo
from django.conf import settings
import re

class LoginObrigatorioMiddleware:

	def process_view(self, request, view_func, view_args, view_kwarg):
		url = request.path_info
		eh_excecao = any(url.startswith(excecao) for excecao in settings.EXEMPT_URLS)

		if  not eh_excecao and \
			not request.user.is_authenticated() and \
			not permite_acesso_anonimo(view_func):

		 	return HttpResponse('Acesso não autorizado', status=401)
