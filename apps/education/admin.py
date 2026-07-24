from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('degree', 'institution')
