from django.contrib import admin
from apps.occurrence.models import Occurrence


class OccurrenceAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'type', 'city', 'state', 'neighborhood', 'street', 'number', 'description', 'date', 'reported_by'
    )
    list_display_links = ('id', 'type')
    search_fields = (
        'type', 'city', 'state', 'neighborhood', 'street', 'number', 'description', 'date', 'reported_by'
    )
    list_per_page = 20


admin.site.register(Occurrence, OccurrenceAdmin)
