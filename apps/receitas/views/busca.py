from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita
from django.contrib import auth, messages

def busca(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas' : lista_receitas
    }
    
    
    return render(request, 'buscar.html', dados)