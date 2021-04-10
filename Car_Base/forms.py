from django import forms
from Car_Base.models import CarBrand, CarModel, PartsCategory, CarParts, PartsAndWork


# Form dla Marki samochodu
class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']

# Form dla tworzenia modeli samochodów
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


#Form dla tworzenia kategorii części
class PartsCategoryForm(forms.ModelForm):
    class Meta:
        model = PartsCategory
        fields = ['name']


#Form dla tworzenia częśći samochodowych
class CarPartsForm(forms.ModelForm):
    class Meta:
        model= CarParts
        fields = '__all__'

# Form do laczenia czesci z montazem
class PartsAndWorkForm(forms.ModelForm):
    class Meta:
        model = PartsAndWork
        fields = '__all__'