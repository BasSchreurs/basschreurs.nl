from django import forms
from .models import GuestbookMessage

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = GuestbookMessage
        fields = ['name', 'message']

