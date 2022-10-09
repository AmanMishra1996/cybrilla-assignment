from django.contrib import admin

from .models import Lead

class LeadAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['lead','']}),
        ('Date information', {'fields': ['created_at','signed_at','closed_at'], 'classes': ['collapse']}),
    ]
    list_display = ('lead', 'created_at')
    list_filter = ['created_at']
    search_fields = ['lead']    


admin.site.register(Lead, LeadAdmin)
