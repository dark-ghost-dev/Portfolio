from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SocialNetwork, SocialUser

@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'name', 'base_url')
    search_fields = ('name', 'slug')
    date_hierarchy = 'created'

@admin.register(SocialUser)
class SocialUserAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('id', 'username', 'social_network', 'profile_url', 'order')
    list_filter = ('social_network',)
    search_fields = ('username', 'social_network__name', 'use')
    ordering = ('order',)
    date_hierarchy = 'created'
    sortable_by = ('order',)