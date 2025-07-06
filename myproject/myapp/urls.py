from django.urls import path
from . import views

# It's a good practice to add an app_name for namespacing
app_name = 'clinic' # Yahan apni app ka naam 'myapp' ya 'clinic' rakhein

urlpatterns = [
    # --- Patient/User Facing URLs ---
    
    # Homepage (displays doctors)
    path('', views.home, name='home'),
    
    # Doctors filtered by specialization (e.g., /specialization/cardiology/)
    path('specialization/<slug:specialization_slug>/', views.doctors_by_specialization, name='doctors_by_specialization'),
    
    # Detail page for a single doctor (e.g., /doctor/12/)
    path('doctor/<int:pk>/', views.doctor_detail, name='doctor_detail'),
    
    # URL to handle appointment request (e.g., /request-appointment/12/)
    path('request-appointment/<int:pk>/', views.request_appointment, name='request_appointment'),
    
    # Page to view all of a patient's appointments
    path('my-appointments/', views.my_appointments, name='my_appointments'),


    # --- Authentication URLs ---
    
    # Signup page
    path('signup/', views.signup_view, name='signup'),
    
    # Login page
    path('login/', views.login_view, name='login'),
    
    # Logout action
    path('logout/', views.logout_view, name='logout'),
]