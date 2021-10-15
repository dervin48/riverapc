from django.contrib import admin
from .models import *



class TipoTelefonoAdmin(admin.ModelAdmin):
    search_fields = ['tipo']

admin.site.register(TipoTelefono,TipoTelefonoAdmin)
# Register your models here.
