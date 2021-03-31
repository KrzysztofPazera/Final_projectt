from django import forms
from Baza_Samochodow.models import CarBrand, CarModel, PartsCategory, CarParts


# Form dla Marki samochodu
class CarBrandForm(forms.ModelForm):
    class Meta:
        model = CarBrand
        fields = ['name']

# Form dla tworzenia modeli samochodów
class CarModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = ['name', 'brand', 'engine']


#Form dla tworzenia kategorii części
class PartsCategoryForm(forms.ModelForm):
    class Meta:
        model = PartsCategory
        fields = ['name']


#Form dla tworzenia częśći samochodowych
class CarPartsForm(forms.ModelForm):
    class Meta:
        model= CarParts
        fields = ['name','car_model', 'id_number_of_product', 'category', 'price']