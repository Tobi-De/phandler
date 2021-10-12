from django.contrib.postgres.fields import ArrayField
from django.db import models
from djmoney.models.fields import MoneyField
from model_utils.models import TimeStampedModel


class Appointment(TimeStampedModel):
    record = models.ForeignKey(
        "records.Record", on_delete=models.CASCADE, related_name="history"
    )
    doctor = models.ForeignKey("records.Doctor", on_delete=models.CASCADE)
    sickness = models.CharField(max_length=255)
    prescriptions = ArrayField(models.CharField(max_length=30), default=list)
    cost = MoneyField(max_digits=14, decimal_places=2, default_currency="XOF")
    date = models.DateTimeField()
    accepted = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.record.patient} - {self.doctor} - {self.date}"
