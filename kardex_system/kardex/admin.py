from django.contrib import admin

from django.contrib import admin
from .models import Compra
from usuarios.models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'saldo', 'is_superuser')
    list_filter = ('is_superuser',)
    search_fields = ('username', 'email')
    ordering = ('-saldo',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_movimiento', 'descripcion', 'monto', 'fecha')
    list_filter = ('tipo_movimiento', 'tienda')
    search_fields = ('descripcion', 'tienda')
    date_hierarchy = 'fecha'
