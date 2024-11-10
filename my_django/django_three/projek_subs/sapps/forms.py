from django import forms
from sapps.models import Costumer

class NewSubscriber(forms.ModelForm):
    class Meta:
        model = Costumer
        fields = "__all__"