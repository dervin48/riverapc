from django.db import models
from .models import *
from persona.models import Persona
from cliente.models import Cliente

class Agendasoporte(models.Model):
    ordensoporte = models.CharField('Orden Soporte',max_length=14, unique=True) 
    cliente = models.ForeignKey(
          Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    fecha_soporte = models.DateField('Fecha Soporte')
    Tiposoporte= models.CharField('Tipo Soporte', max_length=50)
    direccion = models.CharField('direccion', max_length=50)
    unique_together=['ordensoporte']
      
    def __str__(self):
          return "%s : %s" % (self.ordensoporte, self.cliente)


    class Meta:
          db_table = 'soporte'
          verbose_name='soporte'
          verbose_name_plural = 'soportes'

