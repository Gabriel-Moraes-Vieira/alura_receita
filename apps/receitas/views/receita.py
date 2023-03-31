from django.shortcuts import render, redirect, get_object_or_404
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage

def index(request):
    """ Página inicial do site """
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas' : receitas_por_pagina
    } 
    
    
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    """ Responsável pela exibição de receitas """
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }


    return render(request, 'receita.html', receita_a_exibir)

def cria_receita(request):
    """ Responsável por criar novas receitas """
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        imagem_receita = request.FILES['imagem_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita.objects.create(pessoa=user, nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, imagem_receita=imagem_receita)
        receita.save()
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')
    
def deleta_receita(request, receita_id):
    """ Responsável por deletar uma receita """
    receita = get_object_or_404(Receita, pk=receita_id )
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    """ Reponsável por pegar a receita que iremos editar e nos redirecionar para tal """
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = { 'receita':receita }
    return render(request, 'usuarios/edita_receita.html', receita_a_editar)

def atualiza_receita(request):
    """ Responsável por atualizar os ítens da nossa receita já existente """
    if request.method == 'POST':
        receita_id = request.POST['receita_id']
        r = Receita.objects.get(pk=receita_id)
        r.nome_receita = request.POST['nome_receita']
        r.ingredientes = request.POST['ingredientes']
        r.modo_preparo = request.POST['modo_preparo']
        r.tempo_preparo = request.POST['tempo_preparo']
        r.rendimento = request.POST['rendimento']
        r.categoria = request.POST['categoria']
        if 'imagem_receita' in request.FILES:
            r.imagem_receita = request.FILES['imagem_receita']
        r.save()
        return redirect('dashboard')