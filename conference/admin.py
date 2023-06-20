
from django.contrib import admin
from .models import Conference

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'dates', 'location')  # Display these fields in the list view
    search_fields = ('name', 'location')  # Add search functionality for these fields
    list_filter = ('dates',)  # Add filters for the 'dates' field
    ordering = ('-dates',)  # Order conferences by descending dates
