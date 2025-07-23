# Hospital Management System

A robust and user-friendly web application built with Python and Django for managing hospital appointments. This system allows patients to browse doctors by specialization, request appointments, and track their status, while providing administrators with a powerful dashboard to manage doctors and appointments.
## 📸 Project Screenshots

<p align="center">
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Hospital-Management-System-Django-/main/myproject/myapp/static/images/1.jpg" alt="Screenshot 1" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Hospital-Management-System-Django-/main/myproject/myapp/static/images/2.jpg" alt="Screenshot 2" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Hospital-Management-System-Django-/main/myproject/myapp/static/images/3.jpg" alt="Screenshot 3" width="30%" />
  <img src="https://raw.githubusercontent.com/NoorMustafa4556/Hospital-Management-System-Django-/main/myproject/myapp/static/images/4.jpg" alt="Screenshot 4" width="30%" />
</p>

## ✨ Core Features

*   **Patient Authentication:**
    *   Secure user signup and login functionality.
    *   Automatic creation of a `Patient` profile for each new user.
*   **Doctor Directory:**
    *   A dynamic homepage displaying all available doctors.
    *   Doctors are categorized by `Specialization` (e.g., Cardiology, Neurology) for easy browsing.
    *   Search functionality to find specific doctors or specializations.
*   **Appointment System:**
    *   Authenticated patients can request an appointment with any available doctor.
    *   A user can only request an appointment with a specific doctor once if a previous request is still `Pending` or `Approved`.
    *   The request button is disabled if an active appointment already exists.
*   **Patient Dashboard:**
    *   A dedicated "My Appointments" page where patients can view all their requested appointments and see their current status (Pending, Approved, Rejected).
*   **Admin Powerhouse:**
    *   Full control over the system via the Django admin panel.
    *   Admins can create, update, and delete `Doctors` and `Specializations`.
    *   View all `Appointments` and can approve, reject, or mark them as completed.
    *   Ability to set a confirmed date and time for approved appointments.

## 🛠️ Technology Stack

*   **Backend:** Python, Django
*   **Database:** SQLite 3 (Default)
*   **Frontend:** HTML, Bootstrap 5

## 🚀 Getting Started

Follow these steps to set up the project on your local machine for development and testing.

### Prerequisites

*   Python (3.8 or higher)
*   pip (Python package manager)
*   Git (for cloning the repository)

### Installation Guide

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/NoorMustafa4556/Hospital-Management-System-Django-.git
    cd Hospital-Management-System-Django-
    ```

2.  **Create and Activate a Virtual Environment:**
    *   **On Windows:**
        ```bash
        python -m venv env
        .\env\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        python3 -m venv env
        source env/bin/activate
        ```

3.  **Install Required Packages:**
    This command will install all the necessary dependencies listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    This command sets up your database schema based on the models defined in the project.
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser:**
    This account will have full access to the Django admin panel.
    ```bash
    python manage.py createsuperuser
    ```
    You will be prompted to enter a username, email, and password.

6.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Your Hospital Management System will now be live at `http://127.0.0.1:8000/`.

## ⚙️ How to Use the System

### As an Administrator:

1.  Navigate to `http://127.0.0.1:8000/admin/`.
2.  Log in using your superuser credentials.
3.  **First, create some `Specializations`** (e.g., "Cardiology", "Dentistry", "Neurology").
4.  **Next, create new `Doctor` profiles**, providing details like name, schedule, and assign them to a specialization.
5.  Go to the **"Appointments"** section to approve or reject patient requests.

### As a Patient:

1.  Go to the homepage at `http://127.0.0.1:8000/`.
2.  **Sign up** for a new account.
3.  **Log in** with your new credentials.
4.  Browse the list of available doctors or filter by specialization.
5.  Click on a doctor's profile to view details and click the **"Request Appointment"** button.
6.  Visit the **"My Appointments"** page to see the status of all your requests.

## 🤝 How to Contribute

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---
