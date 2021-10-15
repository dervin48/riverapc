 #- * -coding: utf-8 - * -
from django.db import models
from datetime import datetime

class Persona(models.Model):
    nombre = models.CharField('nombres', max_length=50)
    apellido = models.CharField('apellidos', max_length=50)
    fecha_nacimiento = models.DateField('fecha nacimiento')
    correo = models.EmailField('email',null=True, blank=True)
    direccion = models.CharField('direccion', max_length=50,
        null=True, blank=True)


    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

    def save(self, **kwargs):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        if self.correo != None:
            self.correo = self.correo.lower()
        self.direccion = self.direccion.upper()

        super(Persona,self).save()


    def edad(self):
        years = int(
            (datetime.now().date() - self.fecha_nacimiento)
            .days/365.25)
        if years > 18:
            mayoredad=str(years) + 'años= Mayor de Edad'
        else:
            mayoredad=str(years) + 'años=Menor de Edad'
        return '%s' % mayoredad


        

    class Meta():
        abstract = True    

class TipoTelefono(models.Model):
    tipo = models.CharField('tipo telefono', max_length=50)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'tipo_telefono'
        verbose_name='Tipo Telefono'
        verbose_name_plural = 'Tipos de Telefono'
        
    
