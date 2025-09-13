from django.urls import path
from . import views

urlpatterns = [
    # AUTOR
    path('autores/', views.AutorListView.as_view(), name='autor-lista'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor-detalhe'),
    path('autores/novo/', views.AutorCreateView.as_view(), name='autor-criar'),
    path('autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor-atualizacao'),
    path('autores/<int:pk>/excluir/', views.AutorDeleteView.as_view(), name='autor-excluir'),

    # LIVRO
    path('livros/', views.LivroListView.as_view(), name='livro-lista'),
    path('livros/<int:pk>/', views.LivroDetailView.as_view(), name='livro-detalhe'),
    path('livros/novo/', views.LivroCreateView.as_view(), name='livro-criar'),
    path('livros/<int:pk>/editar/', views.LivroUpdateView.as_view(), name='livro-atualizacao'),
    path('livros/<int:pk>/excluir/', views.LivroDeleteView.as_view(), name='livro-excluir'),

    # API EXTERNA - Buscar livro por ISBN
    path('buscar-livro/<str:isbn>/', views.buscar_livro_api, name='buscar-livro-api'),
]
