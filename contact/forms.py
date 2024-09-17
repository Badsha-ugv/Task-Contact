from django import forms 
from .models import ContactBook

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactBook 
        fields = '__all__'

    