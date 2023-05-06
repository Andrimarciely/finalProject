from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)

