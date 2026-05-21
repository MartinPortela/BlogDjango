#blog/views.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
class VistaListaPosts(ListView):
    model = Post
    template_name = "home.html"
class VistaDetallePost(DetailView):
    model = Post
    template_name = "detalle_post.html"
class VistaCrearPost(CreateView): # uevo
    model = Post
    template_name = "nuevo_post.html"
    fields = ["titulo", "autor", "cuerpo"] 
# Campos del modelo Post que se mostrarán en el formulario
class VistaActualizarPost(UpdateView): # nuevo
    model = Post
    template_name = "actualizar_post.html"
    fields = ["titulo", "cuerpo"]
class VistaEliminarPost(DeleteView): # nuevo
    model = Post
    template_name = "eliminar_post.html"
    success_url = reverse_lazy("home")