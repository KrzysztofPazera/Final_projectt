from django.forms import ModelForm
from django.db import models
from .models import Repair_costs, Client
from Car_Base.models import CarBrand, CarModel
from django import forms

#Dodawanie kleinta
class AddClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name']


class RepairCostsForm(ModelForm):
    class Meta:
        model = Repair_costs
        fields= '__all__'
        widgets = {
            'date_of_accident': forms.DateInput(attrs={'type': 'date'})
        }


    # def __init__(self, car_brand, **kwargs):
    #     super(RepairCostsForm, self).__init__(**kwargs)
    #
    #     if car_brand:
    #         self.fields['car_model'].queryset = forms.CarModel.objects.filter(brand=car_brand)


class Step1Form(forms.ModelForm):
    class Meta:
        model = Repair_costs
        fields = ['name_owner',
                  'surname_owner',
                  'date_of_accident',
                  'car_brand']
        widgets = {
            'date_of_accident': forms.DateInput(attrs={'type': 'date'})
        }

class Step2Form(forms.ModelForm):
    class Meta:
        model =Repair_costs
        fields = ['car_model']
