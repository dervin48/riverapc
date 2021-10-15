from django.contrib import admin
from .models import *

class TelefonoInline(admin.TabularInline):
    model = Telefono
    extra = 0 
    autocomplete_fields = ['tipo']

class ClienteAdmin(admin.ModelAdmin):
    inlines = [TelefonoInline] 
    search_fields = ['cliente__nit','apellido']
    list_filter = ['fecha_nacimiento']
    list_display = ['nit','nombre','apellido','fecha_nacimiento','edad','correo']

admin.site.register(Cliente,ClienteAdmin)