from django.contrib import admin
from .models import Commerce


class CommerceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'amount', 'total_price', 'paid_price', 'debt', 'created_at',)
    list_display_links = ('id', 'product')

    list_filter = ('product', 'customer',)


admin.site.register(Commerce, CommerceAdmin)
