from django.urls import path

from . import views

urlpatterns = [
    path("root", views.home, name="root"),
    path("", views.home, name= "home"),
    path("home.html", views.home, name= "home"),
    path("event/", views.EventListView.as_view(), name="event-list"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("<int:year>/<int:month>/<int:day>", views.day, name="agenda-events-day"),
    path("event/new", views.EventCreateView.as_view(), name="event-create"),
    path(
        "event/<int:pk>/edit",
        views.EventUpdateView.as_view(),
        name="event-update",
    ),
    path(
        "event/<int:pk>/delete",
        views.EventDeleteView.as_view(),
        name="event-delete",
    ),
    path("client", views.ClientListView.as_view(), name="client-list"),
    path("client/new", views.ClientCreateView.as_view(), name="client-create"),
    path(
        "client/<int:pk>/edit",
        views.ClientUpdateView.as_view(),
        name="client-update",
    ),
    path(
        "client/<int:pk>/delete",
        views.ClientDeleteView.as_view(),
        name="client-delete",
    ),
    path("matrix", views.MatrixListView.as_view(), name="matrix-list"),
    path("matrix/new", views.MatrixCreateView.as_view(), name="matrix-create"),
    path(
        "matrix/<int:pk>/edit",
        views.MatrixUpdateView.as_view(),
        name="matrix-update",
    ),
    path(
        "matrix/<int:pk>/delete",
        views.MatrixDeleteView.as_view(),
        name="matrix-delete",
    ),
    path("sample", views.SampleListView.as_view(), name="sample-list"),
    path("sample/new", views.SampleCreateView.as_view(), name="sample-create"),
    path(
        "sample/<int:pk>/edit",
        views.SampleUpdateView.as_view(),
        name="sample-update",
    ),
    path(
        "sample/<int:pk>/delete",
        views.SampleDeleteView.as_view(),
        name="sample-delete",
    ),
    path("document", views.DocumentListView.as_view(), name="document-list"),
    path("document/new", views.DocumentCreateView.as_view(), name="document-create"),
    path(
        "document/<int:pk>/edit",
        views.DocumentUpdateView.as_view(),
        name="document-update",
    ),
    path(
        "document/<int:pk>/delete",
        views.DocumentDeleteView.as_view(),
        name="document-delete",
    ),
    path("product", views.ProductListView.as_view(), name="product-list"),
    path("product/new", views.ProductCreateView.as_view(), name="product-create"),
    path(
        "product/<int:pk>/edit",
        views.ProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "product/<int:pk>/delete",
        views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
    path("service", views.ServiceListView.as_view(), name="service-list"),
    path("service/new", views.ServiceCreateView.as_view(), name="service-create"),
    path(
        "service/<int:pk>/edit",
        views.ServiceUpdateView.as_view(),
        name="service-update",
   ),
    path(
       "service/<int:pk>/delete",
       views.ServiceDeleteView.as_view(),
       name="service-delete",
    ),
    path("proposal", views.ProposalListView.as_view(), name="proposal-list"),
    path("proposal/new", views.ProposalCreateView.as_view(), name="proposal-create"),
    path("proposal/proposal_pdf", views.proposal_pdf, name='proposal_pdf'),
    path(
        "proposal/<int:pk>/edit",
        views.ProposalUpdateView.as_view(),
        name="proposal-update",
    ),
    path(
        "proposal/<int:pk>/delete",
        views.ProposalDeleteView.as_view(),
        name="proposal-delete",
    ),
]