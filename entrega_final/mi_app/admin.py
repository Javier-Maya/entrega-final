from django.contrib import admin
from .models import Autor, Libro

# Register your models here.
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'bio')
    list_filter = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'genero', 'descripcion', 'fecha')
    list_filter = ('titulo', 'editorial', 'genero')
    search_fields = ('titulo',)