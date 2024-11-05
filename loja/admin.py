from django.contrib import admin

# Register your models here.
from .models import * #Importará nossos modelos
class FabricanteAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
class ProdutoAdmin(admin.ModelAdmin):
    date_hierarchy = 'criado_em'
    list_display = ('Produto', 'destaque', 'promocao', 'msgpromocao', 'preco', 'categoria',)
    empty_value_display = 'Vazio'
    fields = ('Produto', 'destaque', 'promocao', 'msgpromocao', 'preco', 'categoria',)
    search_fields = ('Produto',)
admin.site.register(Fabricante, FabricanteAdmin) #Adiciona a interface do adm
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
