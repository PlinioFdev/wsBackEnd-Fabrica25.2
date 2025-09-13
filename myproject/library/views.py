from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor, Livro

# ---------------- AUTOR ----------------
class AutorListView(ListView):
    model = Autor
    template_name = "library/autores/autor_list.html"

class AutorDetailView(DetailView):
    model = Autor
    template_name = "library/autores/autor_detail.html"

class AutorCreateView(CreateView):
    model = Autor
    fields = "__all__"
    template_name = "library/autores/autor_form.html"
    success_url = reverse_lazy("autor_list")

class AutorUpdateView(UpdateView):
    model = Autor
    fields = "__all__"
    template_name = "library/autores/autor_form.html"
    success_url = reverse_lazy("autor_list")

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "library/autores/autor_confirm_delete.html"
    success_url = reverse_lazy("autor_list")

# ---------------- LIVRO ----------------
class LivroListView(ListView):
    model = Livro
    template_name = "library/livros/livro_list.html"

class LivroDetailView(DetailView):
    model = Livro
    template_name = "library/livros/livro_detail.html"

class LivroCreateView(CreateView):
    model = Livro
    fields = "__all__"
    template_name = "library/livros/livro_form.html"
    success_url = reverse_lazy("livro_list")

class LivroUpdateView(UpdateView):
    model = Livro
    fields = "__all__"
    template_name = "library/livros/livro_form.html"
    success_url = reverse_lazy("livro_list")

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = "library/livros/livro_confirm_delete.html"
    success_url = reverse_lazy("livro_list")
    
from django.http import JsonResponse
from .services import buscar_livro_por_isbn

def buscar_livro_api(request, isbn):
    dados = buscar_livro_por_isbn(isbn)
    return JsonResponse(dados)
