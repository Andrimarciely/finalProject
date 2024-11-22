from django.contrib import admin
from .models import Event, Document, EnvironmentalConsultancy, Client, Matrix, Sample, Product , Service, Proposal

"""Admin class to customize class's models."""
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "registration_number",
    )
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(EnvironmentalConsultancy)
class EnvironmentalConsultancyAdmin(admin.ModelAdmin):
    list_display = ("corporate_name",)
    list_display_links = ("corporate_name",)
    search_fields = ("corporate_name",)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "corporate_name",
        "responsible_contact",
    )
    list_display_links = ("corporate_name",)
    search_fields = ("corporate_name",)

@admin.register(Matrix)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "client","objective","collection_date")
    list_display_links = ("objective",)
    search_fields = ("objective",)
