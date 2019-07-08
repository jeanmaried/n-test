from django import forms
from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your First Name"
        })
    )
    last_name = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Last Name"
        })
    )
    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('Your Phone #'), 'class': ('form-control')}), label=("Phone number"), required=False)
