from django.urls import path
from kingdom.views import *

urlpatterns = [
    path('', index),
    path('quemsomos/', quemsomos, name='quemsomos'),
    path('ver/', ver, name='ver'),
    path('acolher/', acolher, name='acolher'),
    path('amar/', amar, name='amar'),
    path('ensinar/', ensinar, name='ensinar'),
    path('direcionar/', direcionar, name='direcionar'),
    path('biblia/nvi', nvi, name='biblia/nvi'),
    path('biblia/nvi/<int:livros_id>', palavra , name = 'palavra' ),
    path('comunhao/fora-da-caixa', fora_da_caixa , name='fora-da-caixa'),
]