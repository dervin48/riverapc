from django.contrib import admin
from .models import *


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'marca__marca']
    list_filter = ['marca', 'estado']
    list_display = ['nombre','marca','precio','precio_costo','existencia', 'estado']
    readonly_fields = ['estado']
    actions = ['anular_producto', 'activar_producto']

    def anular_producto(self, request, queryset):
        for row in queryset.filter(estado=True):
            self.log_change(request, row, 'Se anula el producto')
        rows_updated = 0
        
        for obj in queryset:
            if obj.estado:
                obj.estado = False
                obj.save()
                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto fue marcado"
        else:
            message_bit = "%s productos fueron marcados" % rows_updated
        self.message_user(request, "%s como anulado satisfactoriamente"  % message_bit)
    anular_producto.short_description = 'Anular Producto'


    def activar_producto(self, request, queryset):
        for row in queryset.filter(estado=False):
            self.log_change(request, row, 'Se activa el producto')
        rows_updated = 0
        
        for obj in queryset:
            if obj.estado == False:
                obj.estado = True
                obj.save()
                rows_updated += 1

        if rows_updated == 1:
            message_bit = "1 producto fue marcado"
        else:
            message_bit = "%s productos fueron marcados" % rows_updated
        self.message_user(request, "%s como activos satisfactoriamente"  % message_bit)
    activar_producto.short_description = 'Activar Producto'


admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)
