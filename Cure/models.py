from django.db import models
from django.db import models
class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=50, choices=[
        ('Pharmacy', 'Pharmacy'),
        ('Laboratory', 'Laboratory'),
        ('Dentistry', 'Dentistry'),
        ('Surgery', 'Surgery'),
    ])
    preferred_date = models.DateField(null=True, blank=True)
    preferred_time = models.TimeField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    insurance_provider = models.CharField(max_length=100, null=True, blank=True)
    policy_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    appointment_date = models.DateField(auto_now_add=True)
    appointment_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.full_name} on {self.appointment_date}"





# INTERNSHIP APPLICATIONS
class InternshipApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    start_date = models.DateField()
    areas_of_interest = models.CharField(max_length=255)
    intro_letter = models.FileField(upload_to='intro_letters/')

    def __str__(self):
        return self.name




# GET IN TOUCH
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"




