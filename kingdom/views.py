from django.shortcuts import render

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
    return render(request, 'kingdom/biblia/nvi.html')

def fora_da_caixa(request):
    return render(request, 'kingdom/comunhao/foradacaixa.html')