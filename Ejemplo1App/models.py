from django.db import models

# Create your models here.


class Producto(models.Model):
    title= models.CharField( max_length=20 )
    description= models.TextField()
    presio= models.IntegerField()
    stok= models.IntegerField()
    vendido= models.IntegerField()
    image= models.ImageField(default='null',upload_to="producto")

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return f"{self.title}"

class CitaRapida(models.Model):
    nombre= models.TextField()
    cabello= models.TextField()
    fecha= models.DateField()
    hora= models.TimeField()

    def __str__(self):
        return f"{self.nombre}"
    
