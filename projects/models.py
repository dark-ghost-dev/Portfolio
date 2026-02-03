from django.db import models
import os

class ProjectType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        verbose_name = 'Tipo de proyecto'
        verbose_name_plural = 'Tipos de proyectos'

    def __str__(self):
        return self.name
    
class ProjectRole(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        verbose_name = 'Rol en proyecto'
        verbose_name_plural = 'Roles en proyectos'

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Descripción')
    summary = models.CharField(max_length=200, verbose_name='Resumen')
    end_date = models.DateField(verbose_name='Fecha de finalización')
    demo_url = models.URLField(blank=True, verbose_name='URL de demo')
    repository_url = models.URLField(blank=True, verbose_name='URL del repositorio')
    project_type = models.ForeignKey(ProjectType, on_delete=models.PROTECT, related_name='projects', verbose_name='Tipo de proyecto')
    project_role = models.ForeignKey(ProjectRole, on_delete=models.PROTECT, related_name='projects', verbose_name='Rol en proyecto')
    duration = models.IntegerField(verbose_name='Duración en meses')
    team_members = models.IntegerField(verbose_name='Número de miembros del equipo')
    active = models.BooleanField(default=True, verbose_name='Activo')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        ordering = ['order']
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    def __str__(self):
        return self.title

def project_image_path(instance, filename):
    return os.path.join(
        'projects',
        instance.project.slug,
        filename
    )

class ProjectImage(models.Model):
    project = models.ForeignKey('Project', related_name='images', on_delete=models.CASCADE, verbose_name='Proyecto')
    image = models.ImageField(upload_to=project_image_path, verbose_name='Imagen')
    caption = models.CharField(max_length=255, blank=True, verbose_name='Descripción')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        ordering = ['order']
        verbose_name = 'Imagen de proyecto'
        verbose_name_plural = 'Imágenes de proyectos'

    def __str__(self):
        return f"Image for {self.project.title} - {self.caption}"
    
class ProjectCharacteristic(models.Model):
    project = models.ForeignKey('Project', related_name='characteristics', on_delete=models.CASCADE, verbose_name='Proyecto')
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    icon = models.TextField(verbose_name="Ícono", help_text="SVG del ícono")
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        ordering = ['order']
        verbose_name = 'Característica de proyecto'
        verbose_name_plural = 'Características de proyectos'

    def __str__(self):
        return f"{self.title}: {self.description}"
    
class ProjectTechnology(models.Model):
    project = models.ForeignKey('Project', related_name='technologies', on_delete=models.CASCADE, verbose_name='Proyecto')
    name = models.CharField(max_length=100, verbose_name='Nombre')
    icon = models.TextField(verbose_name="Ícono", help_text="SVG del ícono")
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creado')
    modified = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificado')

    class Meta:
        ordering = ['order']
        verbose_name = 'Tecnología de proyecto'
        verbose_name_plural = 'Tecnologías de proyectos'

    def __str__(self):
        return self.name