from django.contrib import admin
from .models import Slider, MisionyVision, Galeria
# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ['cod', 'imagen']
    search_fields = ['cod']
    list_per_page = 10

class MisionyVisionAdmin(admin.ModelAdmin):
    list_display = ['name', 'descripcion']
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['cod','name','descripcion','imagen']
    search_fields = ['cod','name']
    list_per_page = 10

admin.site.register(Slider, SliderAdmin)

admin.site.register(MisionyVision, MisionyVisionAdmin)

admin.site.register(Galeria, GaleriaAdmin)

