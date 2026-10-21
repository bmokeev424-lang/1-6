from django.contrib import admin
from .models import Equipment, MaintenanceRequest

admin.site.register(Equipment)

@admin.register(MaintenanceRequest)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'equipment', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority')
    search_fields = ('description',)