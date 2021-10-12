import django_filters as filters

from .models import Appointment


class AppointmentFilter(filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ["doctor__name", "record__patient__name", "accepted", "date"]
