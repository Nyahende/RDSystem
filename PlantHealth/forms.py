from django import forms
from .models import Permit, User

class PermitForm(forms.ModelForm):
    class Meta:
        model = Permit
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
