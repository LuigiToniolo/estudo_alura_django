from django.urls import path
from galeria.views import index, imagem, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem_name'),
    path('buscar', buscar, name="buscar"),  
]

