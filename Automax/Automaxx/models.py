from django.db import models

# Create your models here.

class Slider(models.Model):
    cod=models.IntegerField(primary_key=True)
    imagen=models.ImageField(upload_to='Slider')

class MisionyVision(models.Model):
    name=models.CharField(max_length=50, primary_key=True)
    descripcion=models.TextField()
    def __str__(self):
        return self.name
class Galeria(models.Model):
    cod=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    descripcion=models.TextField()
    imagen=models.ImageField(upload_to='Galeria', null=True)
    def __str__(self):
        return self.name

