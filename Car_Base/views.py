from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from Car_Base.forms import CarBrandForm, CarModelForm, CarPartsForm, PartsCategoryForm
from Car_Base.models import CarBrand, CarModel, CarParts, PartsCategory


# Strona glowna
def index(request):
    return render(request, 'base.html')


# Widok dodawania marki samochodu
class CarBrandFormView(LoginRequiredMixin, CreateView):
    form_class = CarBrandForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('car_brand_list')


# Widok wyswitlajacy wszystkie marki
class CarBrandListView(View):
    def get(self, request):
        objects = CarBrand.objects.all()
        name = request.GET.get('data')
        cars = CarModel.objects.all()
        # list= {}
        # for obj in objects:
        #     brand_id = obj.id
        #     brand_name=obj.name
        #     print(brand_name)
        #     cars = CarModel.objects.filter(brand=brand_id).count()
        #     print(cars)
        #     list[brand_name]=cars
        #     print(list)

        if name is not None:
            objects = objects.filter(name__incontains=name)
        return render(request, 'car_brad_list.html', {'objects_list': objects})


# Widok dodawania modelu samochodu
class AddCarModelFormView(LoginRequiredMixin, CreateView):
    form_class = CarModelForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('car_brand_list')


# Widoko usuwania marki samochodu
def delete_car_brand(request, id):
    object = CarBrand.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'delete.html', {'objhect': object})
    if request.method == 'POST':
        object.delete()
        return redirect('car_brand_list')


# Widok usuwania modelu samochodu
def delete_car_model(request, id):
    object = CarModel.objects.get(id=id)
    id_obj=object.brand.id
    if request.method == 'GET':
        return render(request, 'delete.html', {'object': object})
    if request.method == 'POST':
        object.delete()
        return redirect('car_list_by_brand', id=id_obj)


# Widok usuwania kategorii czesci
def delete_part_category(request, id):
    object = PartsCategory.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'delete.html', {'object': object})
    if request.method == 'POST':
        object.delete()
        return redirect('parts_category')


# Widok usuwania czesci sam.
def delete_part(request, id):
    object = CarParts.objects.get(id=id)
    id_obj= object.category.id
    if request.method == 'GET':
        return render(request, 'delete.html', {'object': object})
    if request.method == 'POST':
        object.delete()
        return redirect('parts_list', id=id_obj)


# Widok pokazujacy wysztskie samochody danej marki
class CarModelListView(View):
    def get(self, request, id):
        brand = CarBrand.objects.get(id=id)
        cars = CarModel.objects.filter(brand=brand)
        return render(request, 'car_model_list.html', {'cars': cars})


# Widok tworzący kategorie cześci
class PartsCategoyFormView(LoginRequiredMixin, CreateView):
    form_class = PartsCategoryForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('parts_category')


# Widok tworzacy czesc samochodwa
class CarPartsFormView(LoginRequiredMixin, CreateView):
    form_class = CarPartsForm
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('parts_category')


# Widok tworzacy liste kategorii
class PartsCategoryListView(View):
    def get(self, request):
        objects = PartsCategory.objects.all()

        return render(request, 'category_parts_list.html', {'objects_list': objects})


# Widok tworzacy liste czesci
class PartsListView(View):
    def get(self, request, id):
        category = PartsCategory.objects.get(id=id)
        objects = CarParts.objects.filter(category=category)
        return render(request, 'list_parts.html', {'objects_list': objects})


# Widok szczegółów częśći
class PartsDetailView(View):

    def get(self, request, id, id_c):
        category = PartsCategory.objects.get(id=id_c)
        parts = CarParts.objects.filter(id=id)
        return render(request, 'part_detail.html', {'parts': parts, 'category': category})


# Widok edytujący części
class PartsDetailEditeView(LoginRequiredMixin, View):

    def get(self, request, id, id_c):
        parts = CarParts.objects.get(id=id)
        cars = CarModel.objects.all()
        categorys = PartsCategory.objects.all()
        return render(request, 'edit_parts.html', {'parts': parts, 'cars': cars, 'categorys': categorys})

    def post(self, request, id, id_c):
        parts = CarParts.objects.get(id=id)
        name = request.POST.get('name')
        parts_id_num = request.POST.get('parts_id')
        car_id = request.POST.get('car_model')
        car = CarModel.objects.get(id=car_id)
        category_id = request.POST.get('category')
        category = PartsCategory.objects.get(id=category_id)
        price = request.POST.get('price')
        parts.name = name
        parts.id_number_of_product = parts_id_num
        parts.category = category
        parts.car_model = car
        parts.price = price
        parts.save()
        return redirect(reverse('parts_category'))


# Widok pokazujacy szczegułowe dane samochodów
class CarDetailView(View):
    def get(self, request, id, id_m):
        cars = CarModel.objects.filter(id=id)
        brand = CarBrand.objects.get(id=id_m)
        return render(request, 'car_detail.html', {'cars': cars})


# Widok do edytowania samochodów
class CarEditView(LoginRequiredMixin, View):
    def get(self, request, id, id_m):
        brands = CarBrand.objects.all()
        cars = CarModel.objects.get(id=id)
        return render(request, 'car_edit.html', {'cars': cars, 'brands': brands})

    def post(self, request, id, id_m):
        cars = CarModel.objects.get(id=id)
        name = request.POST.get('name')
        brand_id = request.POST.get('car_brand')
        engine = request.POST.get('engine')
        year = request.POST.get('year')
        generacion = request.POST.get('generacion')
        cars.name = name
        brand = CarBrand.objects.get(id=brand_id)
        cars.brand = brand
        cars.year = year
        cars.generacion = generacion
        cars.engine = engine
        cars.save()
        return redirect(reverse('car_brand_list'))
