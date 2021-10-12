import django_filters as filters

from .models import Doctor, Patient, Record


class RecordFilter(filters.FilterSet):
    class Meta:
        model = Record
        fields = ["patient__name"]


class DoctorFilter(filters.FilterSet):
    class Meta:
        model = Doctor
        fields = ["name"]


class PatientFilter(filters.FilterSet):
    class Meta:
        model = Patient
        fields = ["name"]
