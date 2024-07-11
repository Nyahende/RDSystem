from django import forms
from .models import Permit, User

STATION_CHOICES = [
    ('kasumulu', 'Kasumulu'),
    ('songwe', 'Songwe'),
    ('tunduma', 'Tunduma'),
    # Add more station choices as needed
]

TEST_CONDUCTED_CHOICES = [
    ('Pysical Test', 'PHYSICAL TEST'),
    ('Chemical_Test', 'CHEMICAL TEST'),
]
class PermitForm(forms.ModelForm):
    station = forms.ChoiceField(choices=STATION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    test_conducted = forms.ChoiceField(choices=TEST_CONDUCTED_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Permit
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
