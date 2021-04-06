from django import forms
from Workers.models import Types, Workers

# Formularz dla typu pracownika
class TypesForms(forms.ModelForm):
    class Meta:
        model = Types
        fields = ['name']


# Formularz dla pracowników
class WorkersForms(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['name','type', 'price', 'work']
