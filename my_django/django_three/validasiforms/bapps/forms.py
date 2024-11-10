from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

def check_for_lowercase(value):
    if not value.islower():
        raise ValidationError("Nama harus menggunakan huruf kecil")

class FormName (forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5), check_for_lowercase])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Masukkan emailmu lagi:')
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']
        
        if email != vemail:
            raise forms.ValidationError("Email tidak sama")