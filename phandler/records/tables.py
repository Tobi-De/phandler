from django_tables2 import tables

from .models import Doctor, Patient


class DoctorTable(tables.Table):
    class Meta:
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

    def render_specialities(self, value: list[str]) -> str:
        return ", ".join(value)


class PatientTable(tables.Table):
    class Meta:
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

    def render_allergies(self, value: list[str]) -> str:
        return ", ".join(value)
