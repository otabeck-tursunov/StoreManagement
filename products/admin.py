from django.contrib import admin
from .models import Product, ImportProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'import_price', 'export_price', 'amount', 'unit')
    list_display_links = ('id', 'name')

    list_filter = ('brand', 'unit')
    search_fields = ('name', 'brand')


class ImportProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'import_price', 'amount', 'total_price', 'comment', 'created_at')
    list_display_links = ('id', 'product')

    list_filter = ('product', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(ImportProduct, ImportProductAdmin)
