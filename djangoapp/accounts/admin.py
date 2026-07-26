from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'apelido', 'nome_completo', 'is_staff']
    search_fields = ['email', 'apelido', 'nome_completo']
    ordering = ['email']

    # Organiza as abas de edição do usuário no painel admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome_completo', 'apelido', 'foto_perfil', 'banner_cor')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    # Organiza a tela de criação de um novo usuário pelo admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'apelido', 'nome_completo', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
