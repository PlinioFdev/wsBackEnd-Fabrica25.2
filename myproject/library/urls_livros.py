from django.urls import path
from . import views

urlpatterns = [
    path('', views.LivroListView.as_view(), name='livro-list'),
    path('create/', views.LivroCreateView.as_view(), name='livro-create'),
    path('<int:pk>/', views.LivroDetailView.as_view(), name='livro-detail'),
    path('<int:pk>/update/', views.LivroUpdateView.as_view(), name='livro-update'),
    path('<int:pk>/delete/', views.LivroDeleteView.as_view(), name='livro-delete'),
]
