from django.db import models
from django.urls import reverse

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    cuerpo = models.TextField()
    archivo_audio = models.FileField(upload_to='songs/', null=True, blank=True)
    portada = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    def get_absolute_url(self): # nuevo
        return reverse("detalle_post", kwargs={"pk": self.pk})