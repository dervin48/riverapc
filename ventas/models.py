from django.db import models
from cliente.models import Cliente
from producto.models import Producto
from django.db.models import Sum 

            
class Venta(models.Model):
    cliente = models.ForeignKey(
          Cliente, verbose_name='Cliente', on_delete=models.CASCADE)
    fecha_venta = models.DateField('fecha venta')
    numero = models.IntegerField('numero')
    total = models.DecimalField('total', max_digits=10, 
          decimal_places=2,editable=False,default=0.00)
      

    def __str__(self):
          return "%s : %s" % (self.numero, self.fecha_venta)


    class Meta:
          db_table = 'venta'
          verbose_name='venta'
          verbose_name_plural = 'ventas'

      
class DetalleVenta(models.Model):
    venta = models.ForeignKey(
          Venta, verbose_name='Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey(
          Producto, verbose_name='Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField('cantidad')
    preciodesc = models.DecimalField('Precio descuento', max_digits=10,
     decimal_places=2, null = True, blank=True)
    sub_total = models.DecimalField('sub_total', max_digits=10,
     decimal_places=2, default=0.00)
  
    def __str__(self):
            return "%s (%s)" % (self.venta, self.producto)
    
    def save(self, **kwargs):
      if self.preciodesc != None:
        self.sub_total = self.preciodesc * self.cantidad
        super(DetalleVenta, self).save()  
      else:
        self.sub_total = self.producto.precio * self.cantidad
        super(DetalleVenta, self).save()
      
     

class Meta:
      db_table = 'venta_detalle'
      verbose_name='detalle de venta'
      verbose_name_plural ='detalles de venta'