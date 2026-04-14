# cadastro\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Rota da página inicial
    path('', views.index, name='index'),

    # Rota da página 'Contatos'
    path('contato/', views.contato, name='contato'),

    # Rota para cadastrar pessoa
    path('new/', views.adicionar, name='adicionar'),

    # Rota para os detalhes de uma pessoa
    path('pessoa/<int:id>/', views.detalhe, name='detalhe'),

    path('pessoa/<int:id>/editar/', views.editar, name='editar'),

    path('pessoa/<int:id>/deletar/', views.deletar, name='deletar'),
]