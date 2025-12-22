from django.shortcuts import render
from django.http import request
from django.views.generic.base import TemplateView
from DaillyApp.models import Cliente
from django.shortcuts import get_object_or_404

# Create your views here.
def page (request):
    return render(template_name='page.html',request=request)

def dailly (request):
    return render(template_name='dailly.html',request=request)

class myview(TemplateView):
    template_name = "page.html"
    def visualizacao(self,**kwargs):
        contexto = super().visualizacao(kwargs)
        contexto['nome'] = Cliente.objects.all()[:]
        return render(request,template_name='page.html',context=contexto)
    
class redirect_view(TemplateView):
    def redirect(self,*args,**kwargs):
        Cliente = get_object_or_404(Cliente,pk=kwargs["pk"])
        Cliente.nome()
        return super().redirect_view(*args,**kwargs)
