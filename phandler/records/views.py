from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django_filters.views import FilterView
from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin

from .filters import DoctorFilter, PatientFilter, RecordFilter
from .models import Doctor, Patient, Record
from .tables import DoctorTable, PatientTable


class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    fields = [
        "name",
        "id_card_number",
        "gender",
        "age",
        "email",
        "address",
        "phone",
        "allergies",
    ]
    template_name = "records/patient_create.html"
    success_message = "Patient created"
    success_url = reverse_lazy("records:patient_list")


class DoctorCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Doctor
    fields = [
        "name",
        "id_card_number",
        "gender",
        "email",
        "address",
        "phone",
        "specialities",
    ]
    template_name = "records/doctor_create.html"
    success_message = "Doctor created"
    success_url = reverse_lazy("records:doctor_list")


class DoctorListView(LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    table_class = DoctorTable
    filterset_class = DoctorFilter
    queryset = Doctor.objects.all().order_by("-created")
    template_name = "records/doctor_list.html"
    context_object_name = "doctors"


class PatientListView(LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    table_class = PatientTable
    filterset_class = PatientFilter
    queryset = Patient.objects.all().order_by("-created")
    template_name = "records/patient_list.html"
    context_object_name = "patients"


class RecordListView(LoginRequiredMixin, FilterView):
    queryset = Record.objects.all().order_by("-created")
    template_name = "records/list.html"
    filterset_class = RecordFilter
    context_object_name = "records"
    paginate_by = 12


class RecordDetailView(LoginRequiredMixin, DetailView):
    model = Record
    context_object_name = "record"
    template_name = "records/detail.html"
