from django.shortcuts import render

def index(request):
    return render(request, 'kingdom/index.html')

def quemsomos(request):
    return render(request, 'kingdom/quemsomos.html')
