
from .models import Comment
from django import forms

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'phone', 'message']