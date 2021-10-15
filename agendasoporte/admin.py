from django.contrib import admin
from .models import *

class AgendasoporteAdmin(admin.ModelAdmin): 
    search_fields = ['cliente']
    list_filter = ['fecha_soporte']
    list_display = ['cliente']

admin.site.register(Agendasoporte,AgendasoporteAdmin)