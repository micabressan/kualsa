from contextlib import nullcontext
from django.db import models
from django.utils import timezone

class Sliders(models.Model):
    #Modelo para slider de la pagina de inicio
    imagen = models.ImageField(upload_to='pics/%y/%m/%d/')
    titulo = models.CharField(max_length=150, blank=True)
    visible = models.BooleanField()

    def __Str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

class Videos(models.Model):
    #Modelo para el video y el texto de la pagina de inicio
    video = models.FileField(upload_to='vids/%y/%m/%d/')
    texto = models.TextField()
    visible = models.BooleanField()

    def __Str__(self):
        return self.texto

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

class Novedades(models.Model):
    #Modelo para las novedades
    #Falta permitir multiples imagenes
    titulo = models.CharField(max_length= 150)
    texto = models.TextField()
    imagen = models.ImageField(blank=True)
    video = models.FileField(upload_to='vids/%y/%m/%d/')
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"

class Propiedades(models.Model):
    #Modelo para la carga de propiedades
    titulo = models.CharField(max_length=150)
    texto = models.TextField()
    imagen = models.ImageField(blank=True)

    def __Str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Propiedad"
        verbose_name_plural = "Propiedades"

class Representantes(models.Model):
    #Modelo para la carga de representantes
    titulo = models.CharField(max_length=150)
    nombre = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono = models.IntegerField()
    celular = models.IntegerField()
    mail = models.CharField()
    mail_secundario = models.CharField()
    representante = models.CharField()
    pagina = models.CharField()
    pagina_secundaria = models.CharField()

    def __Str__(self):
        return self.titulo
    
    class Meta:
        verboes_name = "Representante"
        verbose_name_plural = "Representantes"
