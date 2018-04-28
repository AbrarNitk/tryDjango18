from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        if not "edu" in email:
            raise forms.ValidationError("Please use Valid email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        print(full_name)
        return "abrar" + full_name

