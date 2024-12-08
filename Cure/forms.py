from django import forms
from .models import Contact
from .models import Appointment
from django import forms
from .models import InternshipApplication
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'full_name', 'contact_number', 'email', 'date_of_birth', 'address',
            'reason', 'department', 'preferred_date', 'preferred_time',
            'insurance_provider', 'policy_number', 'appointment_time'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'preferred_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'insurance_provider': forms.TextInput(attrs={'class': 'form-control'}),
            'policy_number': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})  # Added for appointment_time
        }





class InternshipApplicationForm(forms.ModelForm):
    class Meta:
        model = InternshipApplication
        fields = ['name', 'email', 'phone', 'resume', 'start_date', 'areas_of_interest', 'intro_letter']

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'areas_of_interest': forms.TextInput(attrs={'placeholder': 'e.g., Pediatrics, Research, Surgery'}),
        }






class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=200, required=False, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")

