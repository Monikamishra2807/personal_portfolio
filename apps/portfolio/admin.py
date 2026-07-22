from django.contrib import admin
from .models import Profile, TechCategory, TechStack, SocialLink


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone', 'location', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('name', 'role', 'email')


@admin.register(TechCategory)
class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level', 'order', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name',)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'icon', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('platform',)
