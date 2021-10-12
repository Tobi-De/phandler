from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class Person(TimeStampedModel):
    class Gender(models.TextChoices):
        Male = "Male", _("Male")
        Female = "Female", _("Female")

    name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender.choices, max_length=6)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField()
    id_card_number = models.CharField(max_length=30, unique=True)
    address = models.TextField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Patient(Person):
    age = models.PositiveSmallIntegerField()
    allergies = ArrayField(models.CharField(max_length=30), default=list, blank=True)


class Doctor(Person):
    specialities = ArrayField(models.CharField(max_length=30), default=list)


class Record(TimeStampedModel):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient} - Medical record"

    def get_absolute_url(self) -> str:
        return reverse("records:detail", kwargs={"pk": self.pk})
