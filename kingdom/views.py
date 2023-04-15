from django.shortcuts import render , get_list_or_404, get_object_or_404
from .models import NovoTestamento

def index(request):
    return render(request, 'kingdom/index.html')

def quemsomos(request):
    return render(request, 'kingdom/quemsomos.html')

def ver(request):
    return render(request, 'kingdom/amago/ver.html')

def acolher(request):
    return render(request, 'kingdom/amago/acolher.html')

def amar(request):
    return render(request, 'kingdom/amago/amar.html')

def ensinar(request):
    return render(request, 'kingdom/amago/ensinar.html')

def direcionar(request):
    return render(request, 'kingdom/amago/direcionar.html')

def nvi(request):
    nvt = NovoTestamento.objects.all()
    
    dados = {
        'nvt' : nvt
    }
    return render(request, 'kingdom/biblia/nvi.html', dados)

def palavra(request, livros_id):
    livro = get_object_or_404(NovoTestamento, pk=livros_id)
    
    livro_a_exibir = {
        'nvt' : livro
    }
    return render(request, 'kingdom/biblia/palavra.html', livro_a_exibir)

def fora_da_caixa(request):
    return render(request, 'kingdom/comunhao/foradacaixa.html')