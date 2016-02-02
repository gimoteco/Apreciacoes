from django.http import HttpResponse
from apreciacoes.base import permite_acesso_anonimo

class LoginObrigatorioMiddleware:

	def process_view(self, request, view_func, view_args, view_kwarg):
		if not request.user.is_authenticated() and not permite_acesso_anonimo(view_func):
		 	return HttpResponse('Acesso não autorizado', status=401)
