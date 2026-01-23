from django.db import models
from django.core.exceptions import ValidationError

def validate_base_url(value):
    value = value.strip()

    if value.startswith(('https://', 'mailto:', 'tel:')):
        return

    raise ValidationError(
        "La URL base debe iniciar con https://, mailto: o tel:"
    )

class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Nombre en minúsculas y guión bajo')
    base_url = models.CharField(max_length=255, validators=[validate_base_url], verbose_name='Enlace')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return self.name

class SocialUser(models.Model):
    social_network = models.ForeignKey(SocialNetwork, on_delete=models.PROTECT, verbose_name='Red Social')
    username = models.CharField(max_length=50, verbose_name='Nombre de usuario')
    profile_url = models.CharField(max_length=100, verbose_name='Path del perfil')
    text = models.CharField(max_length=100, verbose_name='Texto')
    additional_info = models.CharField(max_length=100, blank=True, verbose_name='Información adicional')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        ordering = ['order']
        verbose_name = 'Usuario de red social'
        verbose_name_plural = 'Usuarios de redes sociales'

    def __str__(self):
        return f"{self.username} en {self.social_network.name}"