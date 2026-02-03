from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import *

@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'created', 'modified')
    search_fields = ('name',)
    date_hierarchy = 'created'

@admin.register(ProjectRole)
class ProjectRoleAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('name', 'created', 'modified')
    search_fields = ('name',)
    date_hierarchy = 'created'

@admin.register(Project)
class ProjectAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('title', 'project_type', 'project_role', 'end_date', 'active', 'order')
    list_filter = ('project_type', 'project_role', 'active',)
    search_fields = ('title', 'description', 'summary')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)

@admin.register(ProjectImage)
class ProjectImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('project', 'caption', 'order')
    search_fields = ('project__title', 'caption')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)

@admin.register(ProjectCharacteristic)
class ProjectCharacteristicAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('project', 'title', 'modified', 'order')
    search_fields = ('project__title', 'title', 'description')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)

@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('project', 'name', 'modified', 'order')
    search_fields = ('project__title', 'name')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)