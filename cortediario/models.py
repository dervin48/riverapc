from django.db import models

# Create your models here.
class CorteDiario(models.Model):
    monto_inicio = models.DecimalField('Monto de Inicio', max_digits=8, decimal_places=2)
    monto_final = models.DecimalField('Monto final', max_digits=8, decimal_places=2)
    fecha = models.DateField('fecha',null = True, blank = True)
    ventasdeldia = models.CharField('ventas del dia',  max_length=30,default=0.00)

      

    def __str__(self):
          return "%s, %s" % (self.ventasdeldia, self.fecha)
    
    def save(self, **kwargs):
        self.ventasdeldia = abs(self.monto_inicio - self.monto_final) 
        super(CorteDiario, self).save()  
      

    class Meta:
          db_table = 'monto'
          verbose_name='monto'
          verbose_name_plural = 'montos'