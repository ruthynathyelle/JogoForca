from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='homePage'),
    path('tema/<int:pk>/', TemaDetalhesView.as_view(), name='temaDetalhes'),

    path('professor/', ProfessorGeralPageView.as_view(), name='professorGeralPage'),

    path('professor/temas/', ListarTemasView.as_view(), name='listarTemasPage'),
    path('professor/temas/adicionar/', AdicionarTemaView.as_view(), name='adicionarTema'),
    path('professor/temas/editar/<int:pk>/', EditarTemaPageView.as_view(), name='editarTema'),
    path('professor/temas/deletar/<int:pk>/', DeletarTemaPageView.as_view(), name='deletarTema'),

    path('professor/palavras/listar/', ListarPalavrasView.as_view(), name='listarPalavrasPage'),
    path('professor/palavras/adicionar/', AdicionarPalavraView.as_view(), name='adicionarPalavra'),
    path('professor/palavras/editar/<int:pk>/', EditarPalavraPageView.as_view(), name='editarPalavra'),
    path('professor/palavras/deletar/<int:pk>/', DeletarPalavraPageView.as_view(), name='deletarPalavra'),

    path('jogo/forca/<int:pk>/', ForcaGameView.as_view(), name='forcaGame'),
    path('jogo/win/', WinPageView.as_view(), name='winPage'),
    path('jogo/lose/', LosePageView.as_view(), name='losePage'),

    path('relatorio/atividades/', RelatorioAtividadeView.as_view(), name='relatorioAtividade'),
]