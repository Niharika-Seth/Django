# Form based on member model
# Registration form for New member 
from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email', 'plan', 'trainer']
