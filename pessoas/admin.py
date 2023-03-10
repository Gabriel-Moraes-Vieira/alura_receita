from django.contrib import admin
from .models import Pessoa

class ListandoPessoa(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('nome',)
    search_fields = ('nome', 'email',)
    list_per_page = 10

admin.site.register(Pessoa,ListandoPessoa)

class Meta:
    app_label = 'pessoas'