from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.html import format_html

from .models import User

admin.site.unregister(Group)


class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'store', 'branch_name', 'first_name', 'last_name', 'image')
    list_display_links = ('id', 'username')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone_number', 'branch_name', 'store', 'image_path', 'is_superuser',
            'is_staff')}),
    )

    def image(self, obj):
        if obj.image_path:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image_path.url))
        return '-'

    image.short_description = 'Image'


admin.site.register(User, CustomUserAdmin)
