from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin

from .filters import AppointmentFilter
from .forms import AppointmentForm
from .models import Appointment
from .tables import AppointmentTable


class AppointmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = AppointmentForm
    template_name = "appointments/create.html"
    success_message = "New appointments crated"
    success_url = reverse_lazy("appointments:list")


class AppointmentListView(
    LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView
):
    queryset = Appointment.objects.all().order_by("-date")
    filterset_class = AppointmentFilter
    template_name = "appointments/list.html"
    table_class = AppointmentTable
