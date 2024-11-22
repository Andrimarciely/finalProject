from django import forms

from .models import Event, Client, Matrix, Sample, Document, Product, Service, Proposal

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "description",
            "responsible_technician",
            "inital_date",
            "final_date",
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "corporate_name",
            "nickname",
            "address",
            "phone_fax",
            "cnpj",
            "email",
            "responsible_contact",
        ]

class MatrixForm(forms.ModelForm):

    class Meta:
        model = Matrix
        fields = [
            "description"
        ]

class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = [
            "description"
        ]

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = [
            "description"
        ]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "description",
            "price",
        ]

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            "description",
            "price",
       ]

class ProposalForm(forms.ModelForm):

    class Meta:
        model = Proposal
        fields = [
            "id",
            "client",
            "objective",
            "collection_date",
            "legal_basis"
       ]