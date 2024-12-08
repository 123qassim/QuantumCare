from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user as a regular user
            messages.success(request, "Registration successful! You can now log in.")
            login(request, user)  # Optionally log in the user
            return redirect('quantumcare')  # Redirect to the main dashboard or login
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                messages.error(request, "Admin login is not allowed here.")
                return redirect('login')
            login(request, user)
            return redirect('quantumcare')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


# @login_required
# def user_dashboard(request):
#     user = request.user
#     if request.method == "POST":
#         user.first_name = request.POST.get('first_name', user.first_name)
#         user.last_name = request.POST.get('last_name', user.last_name)
#         user.email = request.POST.get('email', user.email)
#         user.save()
#         messages.success(request, "Profile updated successfully!")
#     return render(request, 'dashboard.html', {'user': user})






