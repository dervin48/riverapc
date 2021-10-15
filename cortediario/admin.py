from django.contrib import admin
from .models import *
# Register your models here.
class CorteDiarioAdmin(admin.ModelAdmin):
    search_fields = ['fecha__fecha']
    list_filter = ['ventasdeldia']
    list_display = ['monto_inicio','monto_final','fecha','ventasdeldia']

admin.site.register(CorteDiario, CorteDiarioAdmin)
