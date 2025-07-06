# views.py (UPDATED CODE)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Doctor, Specialization, Patient, Appointment

def create_patient_profile(user):
    if not hasattr(user, 'patient'):
        Patient.objects.create(user=user)

def home(request):
    if request.user.is_authenticated:
        create_patient_profile(request.user)
        search_query = request.GET.get('search', '')
        doctors = Doctor.objects.all()
        if search_query:
            doctors = doctors.filter(
                Q(name__icontains=search_query) | 
                Q(specialization__name__icontains=search_query)
            )
        specializations = Specialization.objects.all()
        context = {
            'doctors': doctors, 'specializations': specializations,
            'search_query': search_query, 'category': None,
        }
        return render(request, 'home.html', context)
    else:
        doctors_sample = Doctor.objects.all()[:10]
        return render(request, 'home.html', {'doctors': doctors_sample})

def doctors_by_specialization(request, specialization_slug):
    specialization = get_object_or_404(Specialization, slug=specialization_slug)
    doctors = Doctor.objects.filter(specialization=specialization)
    specializations = Specialization.objects.all()
    context = {
        'doctors': doctors, 'category': specialization, 'categories': specializations,
    }
    return render(request, 'category_products.html', context)

# === START: UPDATED VIEW LOGIC ===
def doctor_detail(request, pk):
    """
    Shows details of a single doctor and checks if an appointment is already requested.
    """
    doctor = get_object_or_404(Doctor, id=pk)
    already_requested = False
    
    if request.user.is_authenticated:
        create_patient_profile(request.user)
        # YEH LINE LIBRARY WALI LOGIC HAI: Check karo ke 'Pending' ya 'Approved' request hai ya nahi
        already_requested = Appointment.objects.filter(
            patient=request.user.patient, 
            doctor=doctor, 
            status__in=['Pending', 'Approved']
        ).exists()

    context = {
        'doctor': doctor,
        'already_requested': already_requested # Yeh variable template ko bhejein
    }
    return render(request, 'doctor_detail.html', context)

@login_required(login_url='clinic:login')
def request_appointment(request, pk):
    """
    Handles the logic for a patient to request an appointment.
    """
    doctor = get_object_or_404(Doctor, id=pk)
    patient = request.user.patient
    
    # Safety Check: Dobara check karein ke request pehle se to nahi hai
    if Appointment.objects.filter(patient=patient, doctor=doctor, status__in=['Pending', 'Approved']).exists():
        messages.warning(request, f"You already have a pending or approved appointment with Dr. {doctor.name}.")
        return redirect('clinic:doctor_detail', pk=doctor.id)

    Appointment.objects.create(
        patient=patient,
        doctor=doctor,
        reason="Patient requested an appointment."
    )
    
    messages.success(request, f"Your appointment request for Dr. {doctor.name} has been sent successfully!")
    # User ko 'My Appointments' page par bhejein taake woh status dekh sake
    return redirect('clinic:my_appointments')
# === END: UPDATED VIEW LOGIC ===

@login_required(login_url='clinic:login')
def my_appointments(request):
    patient = request.user.patient
    appointments = Appointment.objects.filter(patient=patient).order_by('-date_requested')
    context = {'appointments': appointments}
    return render(request, 'my_appointments.html', context)

# --- Authentication Views (No Change Needed Here) ---
def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('clinic:signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, f"Username '{username}' is already taken.")
            return redirect('clinic:signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, f"An account with email '{email}' already exists.")
            return redirect('clinic:signup')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name; user.last_name = last_name; user.save()
        Patient.objects.create(user=user)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('clinic:login')
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('username_or_email')
        password = request.POST.get('password')
        user = User.objects.filter(Q(username=identifier) | Q(email=identifier)).first()
        if user is not None:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                create_patient_profile(auth_user)
                next_page = request.GET.get('next')
                if next_page: return redirect(next_page)
                return redirect('clinic:home')
            else: messages.error(request, "Invalid password.")
        else: messages.error(request, "Invalid username or email.")
        return redirect('clinic:login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('clinic:home')