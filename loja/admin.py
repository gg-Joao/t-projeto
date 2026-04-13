from django.contrib import admin
from .models import Fabricante, Categoria, Produto


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
	list_display = ('nome',)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome',)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fabricante', 'categoria', 'preco')
