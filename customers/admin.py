from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'store_name', 'phone_number', 'debt',)
    list_display_links = ('id', 'first_name')

    search_fields = ('first_name', 'last_name', 'store_name', 'phone_number')


admin.site.register(Customer, CustomerAdmin)
