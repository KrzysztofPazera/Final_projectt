from django.db.models import Count
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django.views import View
from Baza_Samochodow.forms import CarBrandForm, CarModelForm, CarPartsForm, PartsCategoryForm
from Baza_Samochodow.models import CarBrand, CarModel, CarParts, PartsCategory


# Strona glowna
def index(request):
    return render(request, 'base.html')


# Widok dodawania marki samochodu
class CarBrandFormView(CreateView):
    form_class = CarBrandForm
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('index')


# Widok wyswitlajacy wszystkie marki
class CarBrandListView(View):
    def get(self, request):
        objects = CarBrand.objects.all()
        name = request.GET.get('data')
        cars = CarModel.objects.all()
        # for obj in objects:
        #     id=obj.id
        #     q = CarModel.objects.filter(brand_id=id)
        #     print(len(q))
        if name is not None:
            objects = objects.filter(name__incontains = name)
        return render(request, 'car_brad_list.html', {'objects_list':objects, 'cars':cars})


# Widok dodawania modelu samochodu
class AddCarModelFormView(CreateView):
    form_class = CarModelForm
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('index')

# Widok pokazujacy wysztskie samochody danej marki
class CarModelListView(View):
    def get(self,request, id):
        brand = CarBrand.objects.get(id=id)
        cars = CarModel.objects.filter(brand=brand)
        return render(request, 'car_model_list.html', {'cars':cars})

# Widok tworzący kategorie cześci
class PartsCategoyFormView(CreateView):
    form_class = PartsCategoryForm
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('index')

# Widok tworzacy czesc samochodwa
class CarPartsFormView(CreateView):
    form_class = CarPartsForm
    template_name = 'form.html'
    def get_success_url(self):
        return reverse('index')

# Widok tworzacy liste kategorii
class PartsCategoryListView(View):
    def get(self,request):
        objects = PartsCategory.objects.all()
        return render(request, 'show_objects.html', {'objects_list': objects})


# Widok tworzacy liste czesci
class PartsListView(View):
    def get(self,request, id):
        category = PartsCategory.objects.get(id=id)
        objects = CarParts.objects.filter(category=category)
        return render(request, 'list_parts.html', {'objects_list':objects})


# Widok szczegółów częśći
class PartsDetailView(View):

    def get(self, request, id, id_c):
        category = PartsCategory.objects.get(id=id_c)
        parts= CarParts.objects.filter(id=id)
        return render(request, 'part_detail.html', {'parts':parts, 'category':category})

# Widok edytujący części
class PartsDetailEditeView(UpdateView):

    def get(self, request, id, id_c):
        parts = CarParts.objects.get(id=id)
        cars = CarModel.objects.all()
        categorys= PartsCategory.objects.all()
        return render(request, 'edit_detail.html', {'parts':parts, 'cars':cars, 'categorys':categorys})
    def post(self,request, id, id_c):
        parts = CarParts.objects.get(id=id)
        name= request.POST.get('name')
        parts_id_num= request.POST.get('parts_id')
        car_id= request.POST.get('car_model')
        car= CarModel.objects.get(id= car_id)
        category_id = request.POST.get('category')
        category = PartsCategory.objects.get(name= category_id)
        price= request.POST.get('price')
        parts.name=name
        parts.id_number_of_product= parts_id_num
        parts.category = category
        parts.car_model=car
        parts.price=price
        parts.save()
        return redirect(reverse('index'))

# Widok pokazujacy szczegułowe dane samochodów
class CarDetailView(View):
    def get(self, request, id, id_m):
        cars = CarModel.objects.filter(id=id)
        brand = CarBrand.objects.get(id=id_m)
        return render(request, 'car_detail.html', {'cars':cars})