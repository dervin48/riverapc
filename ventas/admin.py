from django.contrib import admin
from .models import *

# Register your models here.

class DetalleVentaInline(admin.TabularInline):
	model = DetalleVenta
	extra = 0 
	autocomplete_fields = ['producto']

class VentaAdmin(admin.ModelAdmin):
	inlines =[DetalleVentaInline]
	search_fields = ['cliente__nit','cliente__nombre','cliente__apellido']
	list_filter = ['fecha_venta']
	list_display = ['numero','fecha_venta','total','cliente']
	readonly_field = ['total']

admin.site.register(Venta, VentaAdmin)