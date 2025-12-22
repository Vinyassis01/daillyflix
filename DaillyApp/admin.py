from django.contrib import admin
from django.http import HttpResponseRedirect

# Register your models here.
from DaillyApp.models import Cliente
@admin.action(description='nome do cliente')
def client_nome (modeladmin,request,queryset):
    return HttpResponseRedirect(redirect_to='dailly/')

class NomeAdmin(admin.ModelAdmin):
    list_display = ["nome", "email"]
    ordering = ["nome"]
    actions = [client_nome]

admin.site.register(Cliente,NomeAdmin)
