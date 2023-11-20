from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100,verbose_name='Titulo')
    director = models.CharField(max_length=100,verbose_name='Nombre')
    release_date = models.DateField(verbose_name='Fecha de inicio',null=True,default=None)
    banner = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')

    def __str__(self):
        return self.title
    
    