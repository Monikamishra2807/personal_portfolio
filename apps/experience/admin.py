from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'duration', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('role', 'company')
