# admin.py

from django.contrib import admin
from .models import Specialization, Doctor, Patient, Appointment

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'contact')
    search_fields = ('name', 'specialization__name', 'email')
    list_filter = ('specialization',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_email', 'contact')
    search_fields = ('user__username', 'user__email', 'contact')
    
    # User model se fields lene ke liye functions
    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = 'Username'
    get_username.admin_order_field = 'user__username'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'doctor', 'patient', 'status', 'date_requested', 'appointment_date')
    list_filter = ('status', 'date_requested', 'doctor')
    search_fields = ('patient__user__username', 'doctor__name')
    list_editable = ('status', 'appointment_date') # Admin aasaani se status aur date update kar sakta hai
    actions = ['mark_approved', 'mark_rejected']

    def mark_approved(self, request, queryset):
        queryset.update(status='Approved')
    mark_approved.short_description = "Mark selected appointments as Approved"

    def mark_rejected(self, request, queryset):
        queryset.update(status='Rejected')
    mark_rejected.short_description = "Mark selected appointments as Rejected"