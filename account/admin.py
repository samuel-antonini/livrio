from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_trusty')
    list_filter = ('is_staff',)
    list_display_links = ('username',)
    ordering = ('email',)
    search_fields = ('email',)
    list_per_page = 25

    fieldsets = (
        ('Dados', {
            'fields': ('first_name', 'last_name', 'email', 'date_joined', 'activation_key',)
        }),
        ('Status do usuário', {
            'fields': ('is_staff', 'is_superuser', 'is_active', 'is_trusty')
        }),
        ('Avançado', {
            'fields': ('groups', 'user_permissions'),
            'classes': ('collapse', 'extrapretty')
        }),
    )


admin.site.register(User, MyUserAdmin)

admin.site.site_header = 'Livr.io'
admin.site.site_title = 'Livr.io'
admin.site.index_title = 'Ferramentas'
