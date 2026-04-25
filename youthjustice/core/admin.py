from django.contrib import admin
from .models import Youth, Case

@admin.register(Youth)
class YouthAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'status', 'date_registered')
    list_filter = ('status', 'gender', 'date_registered')
    search_fields = ('first_name', 'last_name', 'contact_number', 'email')
    readonly_fields = ('date_registered', 'date_updated')
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender')
        }),
        ('Contact Information', {
            'fields': ('contact_number', 'email', 'address')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('date_registered', 'date_updated'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'youth', 'case_type', 'status', 'court_date', 'date_filed')
    list_filter = ('status', 'case_type', 'court_date', 'date_filed')
    search_fields = ('case_number', 'youth__first_name', 'youth__last_name')
    readonly_fields = ('date_filed', 'date_updated')
    fieldsets = (
        ('Case Information', {
            'fields': ('youth', 'case_number', 'case_type', 'status')
        }),
        ('Case Details', {
            'fields': ('description', 'court_date', 'judge_name', 'outcome')
        }),
        ('Timestamps', {
            'fields': ('date_filed', 'date_updated'),
            'classes': ('collapse',)
        }),
    )

