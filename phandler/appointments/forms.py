from datetime import timedelta

from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            "record",
            "doctor",
            "sickness",
            "prescriptions",
            "cost",
            "accepted",
            "duration",
            "date",
        ]
        widgets = {
            "date": forms.DateTimeInput(attrs={"placeholder": "DD/MM/YYYY HH:MM"})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        date = cleaned_data["date"]
        doctor = self.cleaned_data["doctor"]
        try:
            aps = Appointment.objects.filter(doctor=doctor, date__date=date)
        except Appointment.DoesNotExist:
            pass
        else:
            for ap in aps:
                ap_end = ap.date + timedelta(minutes=ap.duration)
                if ap_end >= date:
                    raise forms.ValidationError(
                        f"Doctor {doctor} have another appointment on "
                        f"the {ap.date} for a duration of {ap.duration}"
                    )
        return cleaned_data
