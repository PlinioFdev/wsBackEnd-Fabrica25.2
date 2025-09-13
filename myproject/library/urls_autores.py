from django.urls import path
from . import views

urlpatterns = [
    path('', views.AutorListView.as_view(), name='autor-list'),
    path('create/', views.AutorCreateView.as_view(), name='autor-create'),
    path('<int:pk>/', views.AutorDetailView.as_view(), name='autor-detail'),
    path('<int:pk>/update/', views.AutorUpdateView.as_view(), name='autor-update'),
    path('<int:pk>/delete/', views.AutorDeleteView.as_view(), name='autor-delete'),
]
