from django.contrib import admin
from .models import *
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.models import PlanEntrenamiento
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

class PlanEntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('persona', 'items_ejercicios')
    def items_ejercicios(self, obj):
      
       return format_html('<a href="/plan/{0}">Ver Plan</a>'.format(obj.id))
        


admin.site.register(PlanEntrenamiento, PlanEntrenamientoAdmin)
admin.site.register(Ejercicio)