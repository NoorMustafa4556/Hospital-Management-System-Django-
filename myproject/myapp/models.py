# models.py (UPDATED - NO IMAGE)

from django.db import models
from django.contrib.auth.models import User

class Specialization(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    schedule = models.CharField(max_length=255, help_text="e.g., Mon-Fri, 9am-5pm")
    # YAHAN SE IMAGEFIELD WALI LINE HATA DI GAYI HAI
    
    def __str__(self):
        return f"Dr. {self.name} ({self.specialization})"

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'), ('Approved', 'Approved'),
        ('Rejected', 'Rejected'), ('Completed', 'Completed'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(null=True, blank=True)
    reason = models.TextField(help_text="Reason for appointment")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient.user.username} with Dr. {self.doctor.name}"