from django.urls import path
from kingdom.views import index , quemsomos

urlpatterns = [
    path('', index),
    path('quemsomos/', quemsomos, name='quemsomos')
]