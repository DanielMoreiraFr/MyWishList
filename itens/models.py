from django.db import models

class Item(models.Model):
    CATEGORIA_CHOICES = [
        ('camisas', 'Camisas'),
        ('calcas', 'Calças'),
        ('bermudas', 'Bermudas'),
        ('sapatos', 'Sapatos'),
        ('acessorios', 'Acessórios'),
        ('acessorios_metalicos', 'Acessórios Metálicos'),
        ('outros', 'Outros'),
    ]

    titulo = models.CharField(
        max_length=255,
        verbose_name='Título',
        )
    
    descricao = models.TextField(
        verbose_name='Descrição',
        )
    
    preco = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço',
    )

    imagem = models.ImageField(
        verbose_name='Imagem',
        upload_to='mural/%Y/%m/', # mudar o formato da data pra ficar mais organizado br
        null=True,
        blank=True,
    )

    alt_texto = models.CharField(
        verbose_name='Texto Alternativo (acessibilidade)',
        max_length=255,
        null=True,
        blank=True,
        help_text='Descreva a imagem para leitores de tela.',
    )

    categoria = models.CharField(
        verbose_name='Categoria',
        max_length=20,
        choices=CATEGORIA_CHOICES,
        default='camisas',        
        )

    data_criacao = models.DateTimeField(
        verbose_name='Criado em',
        auto_now_add=True,
    )
    
    def __str__(self):
        return self.titulo