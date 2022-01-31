from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from . import models


class UserCreateForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': "Username"
        }), label="user name")
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': "Email"
        }
    ), label="email")

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': "Password"
        }
    ), label="password")

    class Meta():
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''


        del self.fields['password2']

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None


class LoginAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': "Username"
        }), label="")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': "Password"
        }
    ), label="")

    class Meta():
        model = get_user_model()
        fields = ['username', 'password']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class BookingForm(forms.ModelForm):



    class Meta():
        model = models.Bookings
        fields = ['car', 'booking_start_date', 'booking_end_date']

        widgets = {
            'booking_start_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_end_date': forms.DateInput(attrs={'type': 'date'})
        }
