from django.db import models

class Marca(models.Model):
    marca = models.CharField('marca', max_length=50)

    def __str__(self):
        return self.marca

    class Meta:
        verbose_name='marca'
        verbose_name_plural ='marcas'

class Producto(models.Model):
    idproducto = models.CharField('Id Producto',max_length=14)
    nombre = models.CharField('nombre', max_length=50)
    marca = models.ForeignKey(
        Marca, verbose_name='Marca', on_delete=models.CASCADE,
        null = True, blank = True)
    precio = models.DecimalField('precio', max_digits=8, decimal_places=2)
    precio_costo = models.DecimalField('precio costo', max_digits=8, decimal_places=2)
    existencia = models.IntegerField('existencia')
    unique_together=['idproducto']
    
    estado = models.BooleanField('estado', default=True)

    #numero = models.PositiveIntegerField(
    #    'numero de Telefono', help_text='solo incluir numeros'
    #)
    #tipo = models.ForeignKey(
    #    TipoTelefono,verbose_name='Tipo Telefono', related_name='TelCliente',on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s : %s-%s" % (self.nombre, self.marca, self.precio)

    class Meta:
        db_table = 'Producto'
        verbose_name='Producto'
        verbose_name_plural ='Productos'
