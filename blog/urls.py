# blog/urls.py
from django.urls import path
from .views import VistaActualizarPost, VistaCrearPost, VistaDetallePost, VistaListaPosts, VistaEliminarPost # nuevo
urlpatterns = [
    path("post/nuevo/", VistaCrearPost.as_view(), name="nuevo_post"), #nuevo
    path("post/<int:pk>/", VistaDetallePost.as_view(),
name="detalle_post"),
    path("post/<int:pk>/actualizar/", VistaActualizarPost.as_view(),
name="actualizar_post"),
    path("post/<int:pk>/eliminar/", VistaEliminarPost.as_view(),
name="eliminar_post"),
    path("", VistaListaPosts.as_view(), name="home")
]