from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nome = models.CharField(
        verbose_name='Nome',
        max_length=255)

    email = models.EmailField(
        verbose_name='Email',
        unique=True
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome']

    def __str__(self):
        return self.nome