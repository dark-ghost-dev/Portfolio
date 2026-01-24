from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SkillCategory, Skill, SocialNetwork, SocialUser

@admin.register(SkillCategory)
class SkillCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'name', 'active', 'order')
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)

@admin.register(Skill)
class SkillAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'name', 'category', 'active', 'order')
    list_filter = ('category', 'active',)
    search_fields = ('name', 'category__name')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'name', 'base_url')
    search_fields = ('name', 'slug')
    date_hierarchy = 'created'

@admin.register(SocialUser)
class SocialUserAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'username', 'social_network', 'profile_url', 'active', 'is_in_footer', 'order')
    list_filter = ('social_network', 'active', 'is_in_footer',)
    search_fields = ('username', 'social_network__name')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)