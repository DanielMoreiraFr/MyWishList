from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'apelido', 'nome_completo', 'foto_perfil', 'banner', 'banner_cor')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'apelido', 'nome_completo', 'foto_perfil', 'banner', 'banner_cor', 'is_public')
