import uuid

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView
import requests
from Repair_estimate.models import Repair_costs, Client, OrderItem, Order
from Car_Base.models import CarModel, CarBrand, CarParts, PartsCategory
from Workers.models import Workers, Types
from .forms import Step2Form, Step1Form, RepairCostsForm, AddClientForm
from datetime import date
import datetime
from random import random
import string

# Sprawdzanie czy dane z form sa prawidlowe
def is_valid_query(param):
    return param != '' and param is not None

# Filtorwanie wynikow
def filter(request):
    qs = CarParts.objects.all()
    parts_category = PartsCategory.objects.all()
    models = CarModel.objects.all()
    brands = CarBrand.objects.all()
    part_name_query = request.GET.get('name')
    car_brand = request.GET.get('car_brands')
    model_query =request.GET.get('car_model')
    category_query = request.GET.get('part_category')



    if is_valid_query(part_name_query):
        qs = qs.filter(name__icontains=part_name_query)

    if is_valid_query(category_query) and category_query != 'Wybierz...':
        qs = qs.filter(category__name=category_query)

    if is_valid_query(model_query) and model_query != 'Wybierz...':
        qs = qs.filter(car_model = model_query)

    if is_valid_query(car_brand) and car_brand != 'Wybierz...':
        qs = qs.filter(car_model__brand__name=car_brand)




    return qs
# Lista czesc z filtorwaniem
@login_required
def car_filter_view(request):
    car_parts_cat={ cat.name : CarParts.objects.filter(category=cat ) for cat in PartsCategory.objects.iterator()}

    qs = filter(request)
    context = {
    'queryset': qs,
    'car_brands': CarBrand.objects.all(),
    'car_model': CarModel.objects.all(),
    'part_category': PartsCategory.objects.all(),
    'car_parts_cat':car_parts_cat
    }
    return render(request, "filter_form.html", context)

# Dodawanie klienta (nie uzywane)

class AddClientView(LoginRequiredMixin, CreateView):
    form_class = AddClientForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse('index')
# Wybieranie klienta( nie uzywane)
def set_client(request):
    client = Client.objects.all()

    context = {
        'clients':client
    }
    return render(request, 'set_client.html', context)
# Dodawanie klienta (nie uzywane)
def add_client(request, **kwargs):
    client = Client.objects.filter(id=kwargs.get('id')).first()

    client_order = Order.objects.get_or_create(client=client, is_ordered=False)
    cl =Order.objects.get(client=client)
    return redirect('repair_list')
# Lista napraw (nie uzywane)
@login_required
def repair_list_view(request):
    car_parts= CarParts.objects.all()
    client = Client.objects.all()

    context ={
        'car_parts':car_parts,
        'clients':client,
        'car_parts_cat':car_parts_cat,
    }

    return render(request,'repair_list.html', context)
def generate_order_id():
    return uuid

# Dodawanie do listy kosztow (nie uzywane)
@login_required
def add_to_cart_view(request, **kwargs):
    order_it = OrderItem.objects.all()
    order_product = CarParts.objects.filter(id=kwargs.get('id')).first()

    try:
        part =OrderItem.objects.get(product=order_product)
        quantiti= part.quantiti
        part.quantiti= quantiti+1
        part.save()

    except:
        order_iteam = OrderItem.objects.create(product=order_product)


    return redirect(reverse('car_filter'))

# Widok z lista kosztow
@login_required
def sumary_list(request):
    order_team = OrderItem.objects.all()
    quantiti_list = []
    for qua in order_team:
        q= qua.quantiti
        quantiti_list.append(q)
    quantiti_total = sum(quantiti_list)
    sum_list = []
    for o in OrderItem.objects.all():
        s =o.product.price
        q =o.quantiti
        suma=s*q
        sum_list.append(suma)
    sum_total =sum(sum_list)

    context = {
        'order_iteam':order_team,
        'sum_total':sum_total,
        'quantiti_total':quantiti_total
    }
    return render(request,'order_list.html', context)
# Usuwanie calości z  listy
def delete_full_from_list(request, id):
    item_to_delete = OrderItem.objects.filter(pk=id)

    if item_to_delete.exists():
        item_to_delete[0].delete()

    return redirect(reverse('sumary_list'))

# Usuwanie jednej sztuki
def delete_from_list(request, id):
    item_to_delete = OrderItem.objects.get(pk=id)

    quantiti= item_to_delete.quantiti
    if quantiti >1:
        item_to_delete.quantiti= quantiti-1
        item_to_delete.save()
    else:
        item_to_delete.delete()




    return redirect(reverse('sumary_list'))

def updata_in_list(request, id):
    item_to_updata = OrderItem.objects.get(pk=id)
    quantiti= item_to_updata.quantiti
    item_to_updata.quantiti= quantiti+1
    item_to_updata.save()

    return redirect(reverse('sumary_list'))
# import json
# class MyEncoder(JSONEncoder):
#         def default(self, o):
#             return o.__str__()




# def step1(request):
#     initial={'name_owner': request.session.get('name_owner', None),
#              'surname_owner':request.session.get('surname_owner',None),
#              'date_of_accident':request.session.get('date_of_accident',None),
#              'car_brand':request.session.get('car_brand',None)}
#     form = Step1Form(request.POST or None, initial=initial)
#     if request.method == 'POST':
#         if form.is_valid():
#             request.session['name_owner'] = form.cleaned_data['name_owner']
#             request.session['surname_owner'] = form.cleaned_data['surname_owner']
#             request.session['date_of_accident'] = MyEncoder().encode(form.cleaned_data['date_of_accident'])
#             request.session['car_brand'] = MyEncoder().encode(form.cleaned_data['car_brand'])
#
#             return HttpResponseRedirect(reverse('secund_step'))
#     return render(request,'form.html', {'form': form})

    # if request.method == 'GET':
    #     car_brand_id = json.loads(request.session['car_brand'])
    #     # print(car_brand_id)
    #     car_brand = CarBrand.objects.get(name=car_brand_id)
    #     # print(car_brand)
    #     models = CarModel.objects.filter(brand=car_brand)
    #     # print(models)
    #     initial = {'car_models': request.session.get('car_models', None)
    #     return render(request, 'step_2.html', {'models':models})
    # return HttpResponseRedirect(re)
    # else:
    #     if form.is_valid():
    #         pet.owner = person
    #         pet.save()
    #         return HttpResponseRedirect(reverse('finished'))
    # return render(request, 'step2.html', {'form': form, ')


