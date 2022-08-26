from django import forms
from .models import ContactProfile

class ContactForm(forms.ModelForm):
  class Meta:
    model = ContactProfile 
    fields = ("name", "email", "message")
    
    widgets = {
      "name ": forms.TextInput(
        attrs={
          "placeholder": "Full Name..",
        }),
      "email": forms.EmailInput(
        attrs={
          "placeholder": "Email Address..",
        }),
      "message": forms.Textarea(
        attrs={
          "row": 6,
          "placeholder": "Message..",
        }),
    }