from django.contrib import admin
from django.contrib import admin

admin.site.site_header = "Panel de Administración - FuturoTrader"
admin.site.site_title = "FuturoTrader Admin"
admin.site.index_title = "Bienvenido al Panel de Control"

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'creado')
    search_fields = ('nombre', 'correo')
    list_filter = ('creado',)