from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser

# Get the custom user model (or default User model if not customized)
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'insurance_provider', 'insurance_number', 'spouse', 'children', 'location']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = False  # Ensure the user is not a staff member
        user.is_superuser = False  # Ensure the user is not a superuser
        if commit:
            user.save()
        return user



# class CustomUserCreationForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
#     )
#     password2 = forms.CharField(
#         label="Confirm Password",
#         widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'})
#     )
#
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password1', 'password2']
