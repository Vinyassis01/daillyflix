from django.shortcuts import render
from django.http import request
from django.views.generic.base import TemplateView
from DaillyApp.models import Momentos,Filmes,Serie,Temporada

class momentos(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		contexto = super().get_context_data(**kwargs)
		contexto["momentos"] = Momentos.objects.all()[:10]
		return contexto

