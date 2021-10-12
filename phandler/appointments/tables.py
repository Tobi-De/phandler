from django_tables2 import tables

from .models import Appointment


class AppointmentTable(tables.Table):
    class Meta:
        model = Appointment
        fields = [
            "record",
            "doctor",
            "sickness",
            "prescriptions",
            "cost",
            "accepted",
            "date",
        ]

    def render_prescriptions(self, value: list[str]) -> str:
        return ", ".join(value)
