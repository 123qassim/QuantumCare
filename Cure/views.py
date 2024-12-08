from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO
from .models import Contact
from django.contrib import messages
from .forms import ContactForm
from django.contrib import messages
from .forms import InternshipApplicationForm
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AppointmentForm
# Create your views here.

# WELCOME SMS
# def home(request):
#     return HttpResponse("Welcome to QuantumCare!")

def hospital(request):
    return render(request, 'hospital.html')


# DENTISTRY

def dental_home(request):
    return render(request, 'dentistry/dentalhome.html')

def dental_about(request):
    return render(request, 'dentistry/dentalabout.html')

def dental_services(request):
    return render(request, 'dentistry/dentalservices.html')

def dental_doctors(request):
    return render(request, 'dentistry/dentaldoctors.html')

def dental_blog(request):
    return render(request, 'dentistry/dentalblog.html')



# LABORATORY
def lab_home(request):
    return render(request, 'laboratory/labindex.html')

def lab_about(request):
    return render(request, 'laboratory/lababout.html')

def lab_contact(request):
    return render(request, 'laboratory/labcontact.html')

def lab_doctors(request):
    return render(request, 'laboratory/labdoctors.html')

def lab_departments(request):
    return render(request, 'laboratory/labdepartments.html')


# DEPARTMENTS
def depart_home(request):
    return render(request, 'departments/departindex.html')

def depart_about(request):
    return render(request, 'departments/departabout.html')

def depart_contact(request):
    return render(request, 'departments/departcontact.html')

def depart_doctors(request):
    return render(request, 'departments/departdoctors.html')

def depart_news(request):
    return render(request, 'departments/departnews.html')

def depart_action(request):
    return render(request, 'departments/departaction.html')



# PHARMACY

def pharmacy_index(request):
    return render(request, 'pharmacy/pharmacyindex.html')

def pharmacy_about(request):
    return render(request, 'pharmacy/pharmacyabout.html')

def pharmacy_cart(request):
    return render(request, 'pharmacy/pharmacycart.html')

def pharmacy_checkout(request):
    return render(request, 'pharmacy/pharmacycheckout.html')



def pharmacy_main(request):
    return render(request, 'pharmacy/pharmacymain.html')

def pharmacy_shop(request):
    return render(request, 'pharmacy/pharmacyshop.html')

def pharmacy_shopsingle(request):
    return render(request, 'pharmacy/pharmacyshop-single.html')

def pharmacy_thankyou(request):
    return render(request, 'pharmacy/pharmacythankyou.html')

# APPOINTMENT BOOKING
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()


            subject = "Appointment Confirmation"
            message = f"""
            Dear {appointment.full_name},

            Your appointment has been successfully booked with the following details:
            - Date: {appointment.preferred_date}
            - Time: {appointment.preferred_time}
            - Department: {appointment.department}

            Thank you for choosing QuantumCare!

            Regards,
            QuantumCare Team
            """
            recipient = appointment.email
            sender = settings.EMAIL_HOST_USER


            send_mail(subject, message, sender, [recipient], fail_silently=False)

            admin_subject = "New Appointment Booked"
            admin_message = f"""
            A new appointment has been booked by {appointment.full_name}.
            Details:
            - Full Name: {appointment.full_name}
            - Department: {appointment.department}
            - Date: {appointment.preferred_date}
            - Time: {appointment.preferred_time}
            - Contact Info: {appointment.contact_number}, {appointment.email}
            """
            admin_recipient = settings.ADMIN_EMAIL
            send_mail(admin_subject, admin_message, sender, [admin_recipient], fail_silently=False)


            return render(request, 'appointment_success.html', {'appointment': appointment})

    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})


def index_view(request):
    return render(request, 'labindex.html')




def blog1(request):
    return render(request, 'dentistry/blog1.html')

def blog2(request):
    return render(request, 'dentistry/blog2.html')

def blog3(request):
    return render(request, 'dentistry/blog3.html')

def quantumcare(request):
    return render(request, 'quantumcare_home.html')




# INTERNSHIP APPLICATION

def apply_internship(request):
    if request.method == 'POST':
        form = InternshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the application
            application = form.save()


            subject = "Internship Offer and Onboarding Details at QuantumCare Hospital"
            body = f"""
Dear {application.name},

We are delighted to inform you that your application for an internship opportunity at 
QuantumCare Hospital has been reviewed and approved. Congratulations on this 
achievement, and welcome to our team!

As part of your onboarding process, we kindly request you to bring the following documents 
and items on your reporting day:
1. *Identification Card*: For verification purposes.
2. *Academic Certificates*: A copy of your academic achievements.
3. *Internship Recommendation Letter*: From your institution or relevant authority.
4. *Lab Coat*: To comply with hospital protocols and maintain professionalism.

- Reporting Date and Time: {application.start_date}
- Reporting Venue: {application.areas_of_interest} Department

During your internship, you will have the opportunity to:
- Gain hands-on experience in a professional healthcare environment.
- Work alongside skilled healthcare professionals dedicated to patient care and medical excellence.
- Enhance your skills and knowledge in.

We take pride in fostering a collaborative and supportive environment that encourages 
learning and growth.

Should you have any questions or require further assistance before your reporting day, 
please do not hesitate to contact us.

We are excited to have you on board and look forward to your contributions to QuantumCare Hospital.

Warm regards,  
QuantumCare Hospital Team
"""


            buffer = BytesIO()
            pdf = canvas.Canvas(buffer, pagesize=A4)


            pdf.setFillColorRGB(0.9, 0.9, 0.95)
            pdf.rect(0, 0, A4[0], A4[1], fill=True, stroke=False)


            pdf.setFont("Helvetica-Bold", 100)
            pdf.setFillColorRGB(0.7, 0.7, 0.7)
            pdf.saveState()
            pdf.translate(A4[0] / 2, A4[1] / 2)
            pdf.rotate(45)
            pdf.drawCentredString(0, 0, "QuantumCare")
            pdf.restoreState()


            pdf.setFont("Helvetica-Bold", 20)
            pdf.setFillColorRGB(0, 0, 0)
            pdf.drawCentredString(A4[0] / 2, A4[1] - 50, "QuantumCare Hospital")
            pdf.setFont("Helvetica", 12)
            pdf.drawCentredString(A4[0] / 2, A4[1] - 70, "123 Main Street, Voi Town")
            pdf.drawCentredString(A4[0] / 2, A4[1] - 85, "P.O. Box 4567, Taita Taveta")


            logo_path = 'static/images3/logo.png'
            try:
                # Move the logo further down
                pdf.drawImage(logo_path, A4[0] / 2 - 60, A4[1] - 180, width=120, height=80, mask='auto')
            except FileNotFoundError:
                pdf.drawString(50, A4[1] - 120, "Logo not found.")


            pdf.setFont("Helvetica", 12)
            y_position = A4[1] - 200
            lines = body.split('\n')
            for line in lines:
                pdf.drawString(50, y_position, line.strip())
                y_position -= 20


            pdf.save()
            buffer.seek(0)
            pdf_file = buffer.getvalue()
            buffer.close()


            email = EmailMessage(
                subject,
                body,
                'QuantumCare Hospital <otahacharles@gmail.com>',
                [application.email],
            )
            email.attach('Offer_Letter.pdf', pdf_file, 'application/pdf')
            email.send()


            response = HttpResponse(
                pdf_file, content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment; filename="Offer_Letter.pdf"'
            return response

    else:
        form = InternshipApplicationForm()
    return render(request, 'internship_form.html', {'form': form})





def pharmacy_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()

            messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
            return redirect('pharmacy_contact')
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'pharmacy/pharmacycontact.html', {'form': form})





