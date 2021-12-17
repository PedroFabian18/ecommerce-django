from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length = 20, unique = True) #unique para que no se repita el valor
    descripcion = models.CharField(max_length = 255, blank = True)
    slug = models.CharField(max_length = 100, unique = True) # Se utiliza para estar dentro de la parte final de la url que representa a la entidad
    cat_imagen = models.ImageField(upload_to = 'photos/categorias', blank = True)

# Para tomar el slug y hacer el filtrado en el navbar para que se muestre en la tienda,ejempplo: http://localhost:8000/tienda/computadoras
    def get_url(self):
        return reverse('productos_por_categoria', args = [self.slug])

    def __str__(self):
        return self.categoria_nombre
