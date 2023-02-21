from django.contrib import admin
from .models import Receita

class ListandoReceita(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'nome_receita', 'categoria', 'publicada')
    list_editable = ('publicada',)
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    
admin.site.register(Receita, ListandoReceita)
