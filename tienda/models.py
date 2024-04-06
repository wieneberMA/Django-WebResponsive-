from django.db import models

# Create your models here.

class CategoriasProdructos(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    update =  models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'CategoríaPro'
        verbose_name_plural = 'CategoríasPro'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categorias=models.ForeignKey(CategoriasProdructos,on_delete= models.CASCADE)
    imagen=models.ImageField(upload_to='tienda',null=True,blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update =  models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

