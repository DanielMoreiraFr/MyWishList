import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


def caminho_foto_perfil(instance, filename):
    extensao = filename.split('.')[-1]
    if instance.apelido:
        nome_arquivo = f"{instance.apelido}_profile_pic.{extensao}"
        return f'profile_pics/{nome_arquivo}'


def caminho_banner_perfil(instance, filename):
    extensao = filename.split('.')[-1]
    if instance.apelido:
        nome_arquivo = f"{instance.apelido}_banner_pic.{extensao}"
        return f'banner_pics/{nome_arquivo}'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    nome_completo = models.CharField(max_length=100)
    apelido = models.CharField(max_length=50, unique=True)
    foto_perfil = models.ImageField(upload_to=caminho_foto_perfil, blank=True, null=True)
    banner = models.ImageField(upload_to=caminho_banner_perfil, blank=True, null=True)
    banner_cor = models.CharField(max_length=7, default='#30706F')
    is_public = models.BooleanField(default=True)
    share_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['apelido', 'nome_completo']

    objects = CustomUserManager()

    def __str__(self):
        return f'@{self.apelido}'
