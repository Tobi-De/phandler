from django.urls import path

from . import views

app_name = "records"
urlpatterns = [
    path("doctor-create/", views.DoctorCreateView.as_view(), name="doctor_create"),
    path("patient-create/", views.PatientCreateView.as_view(), name="patient_create"),
    path("record-list/", views.RecordListView.as_view(), name="list"),
    path("record-detail/<int:pk>/", views.RecordDetailView.as_view(), name="detail"),
    path("patient-list/", views.PatientListView.as_view(), name="patient_list"),
    path("doctor-list/", views.DoctorListView.as_view(), name="doctor_list"),
]
