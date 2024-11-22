from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Event, Client, Matrix, Sample, Document, Product , Service, Proposal
from .forms import EventForm, ClientForm, MatrixForm, SampleForm, DocumentForm, ProductForm, ServiceForm, ProposalForm
from datetime import datetime, timedelta
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

#Import PDF stuff

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#Generate PDF
def proposal_pdf(request):
    #Create Bytestream buffer
    buf=io.BytesIO()
    #Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    #Add some lines of text
    #lines = [
    #    "This is line 1",
    #    "This is line 2",
    #    "This is line 3",
    # ]
    #Designate The Model
    proposals = Proposal.objects.all()

    #Create blank list
    lines = []
    #Loop

    for proposal in proposals:
        lines.append(f"Cliente: {proposal.client}")
        lines.append(f"Objetivo: {proposal.objective}")
        lines.append(f"Data de Coleta: {proposal.collection_date.strftime('%d/%m/%Y')}")
        lines.append(f"Base Legal: {proposal.legal_basis}")
        lines.append(" ")


    for line in lines:
        textob.textLine(line)

    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename='proposal.pdf')


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Andrimarciely"
    month = month.capitalize()

    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number, withyear = True)

    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%H:%M')

    return render(request,'home.html',{
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
        })


def dashboard(request):
    return render(request,'dashboard.html')


def day(request, year: int, month: int, day: int):
    """
    Visualização dos eventos de um determinado dia, recebe a data em
    formato ano/mês/dia como parâmtro.
    """
    day = datetime(year, month, day)
    filted_events = Event.objects.filter(
        date="{:%Y-%m-%d}".format(day)
    ).order_by("-priority", "event")

    context = {
        "today": localdate(),
        "day": day,
        "events": filted_events,
        "next": day + timedelta(days=1),
        "previous": day - timedelta(days=1),
        "priorities": Event.priorities_list,
    }

    return render(request, "day.html", context)


class DeleteRecordMixin:

    def post(self, request, pk):
        record = get_object_or_404(self.model, pk=pk)
        record.delete()

        return redirect(self.success_url)


class EventViewMixin:
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("event-list")


class EventCreateView(EventViewMixin, CreateView):
    ...


class EventListView(EventViewMixin, ListView):
    ...

class EventUpdateView(EventViewMixin, UpdateView):
    ...
class EventView(EventViewMixin, DeleteRecordMixin, DeleteView):
    ...

class EventDeleteView(EventViewMixin, DeleteRecordMixin, DeleteView):
    ...



class ClientViewMixin:
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("client-list")


class ClientCreateView(ClientViewMixin, CreateView):
    ...


class ClientListView(ClientViewMixin, ListView):
    ...

class ClientUpdateView(ClientViewMixin, UpdateView):
    ...
class ClientView(ClientViewMixin, DeleteRecordMixin, DeleteView):
    ...

class ClientDeleteView(ClientViewMixin, DeleteRecordMixin, DeleteView):
    ...


class MatrixViewMixin:
    model = Matrix
    form_class = MatrixForm
    success_url = reverse_lazy("matrix-list")


class MatrixCreateView(MatrixViewMixin, CreateView):
    ...


class MatrixListView(MatrixViewMixin, ListView):
    ...

class MatrixUpdateView(MatrixViewMixin, UpdateView):
    ...
class MatrixView(MatrixViewMixin, DeleteRecordMixin, DeleteView):
    ...

class MatrixDeleteView(MatrixViewMixin, DeleteRecordMixin, DeleteView):
    ...

class SampleViewMixin:
    model = Sample
    form_class = SampleForm
    success_url = reverse_lazy("sample-list")


class SampleCreateView(SampleViewMixin, CreateView):
    ...


class SampleListView(SampleViewMixin, ListView):
    ...

class SampleUpdateView(SampleViewMixin, UpdateView):
    ...
class SampleView(SampleViewMixin, DeleteRecordMixin, DeleteView):
    ...

class SampleDeleteView(SampleViewMixin, DeleteRecordMixin, DeleteView):
    ...

class DocumentViewMixin:
    model = Document
    form_class = DocumentForm
    success_url = reverse_lazy("document-list")


class DocumentCreateView(DocumentViewMixin, CreateView):
    ...


class DocumentListView(DocumentViewMixin, ListView):
    ...

class DocumentUpdateView(DocumentViewMixin, UpdateView):
    ...
class DocumentView(DocumentViewMixin, DeleteRecordMixin, DeleteView):
    ...

class DocumentDeleteView(DocumentViewMixin, DeleteRecordMixin, DeleteView):
    ...


class ProductViewMixin:
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product-list")


class ProductCreateView(ProductViewMixin, CreateView):
    ...


class ProductListView(ProductViewMixin, ListView):
    ...

class ProductUpdateView(ProductViewMixin, UpdateView):
    ...
class ProductView(ProductViewMixin, DeleteRecordMixin, DeleteView):
    ...

class ProductDeleteView(ProductViewMixin, DeleteRecordMixin, DeleteView):
    ...


class ServiceViewMixin:
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy("service-list")


class ServiceCreateView(ServiceViewMixin, CreateView):
    ...


class ServiceListView(ServiceViewMixin, ListView):
    ...

class ServiceUpdateView(ServiceViewMixin, UpdateView):
    ...
class ServiceView(ServiceViewMixin, DeleteRecordMixin, DeleteView):
    ...

class ServiceDeleteView(ServiceViewMixin, DeleteRecordMixin, DeleteView):
    ...


class ProposalViewMixin:
    model = Proposal
    form_class = ProposalForm
    success_url = reverse_lazy("proposal-list")


class ProposalCreateView(ProposalViewMixin, CreateView):
    ...


class ProposalListView(ProposalViewMixin, ListView):
    ...

class ProposalUpdateView(ProposalViewMixin, UpdateView):
    ...
class ProposalView(ProposalViewMixin, DeleteRecordMixin, DeleteView):
    ...

class ProposalDeleteView(ProposalViewMixin, DeleteRecordMixin, DeleteView):
    ...