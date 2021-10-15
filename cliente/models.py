 #- * -coding: utf-8 - * -
from django.db import models
from persona.models import Persona, TipoTelefono

# Create your models here.

class Cliente (Persona):
    nit = models.CharField('nit', max_length=10, unique=True)
    unique_together=['nit']
    
    class Meta():
        db_table = 'cliente'
        verbose_name='Cliente'
        verbose_name_plural = 'Clientes'

class Telefono(models.Model):
    cliente = models.ForeignKey(
        Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    numero = models.PositiveIntegerField(
        'numero de Telefono', help_text='solo incluir numeros'
    )
    tipo = models.ForeignKey(
        TipoTelefono,verbose_name='Tipo Telefono', related_name='TelCliente',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s : %s" % (self.cliente, self.numero)

    class Meta:
        verbose_name='Telefono de cliente'
        verbose_name_plural = 'Telefonos de cliente'