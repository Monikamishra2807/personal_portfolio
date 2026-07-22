from django.contrib import admin
from .models import Project, ProjectTag


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active')
    search_fields = ('title', 'short_description')
    filter_horizontal = ('tech_stack', 'tags')


@admin.register(ProjectTag)
class ProjectTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name',)
