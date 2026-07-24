from django.contrib import admin
from .models import Certification


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date', 'order', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'issuer')
