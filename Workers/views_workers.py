from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView

from Workers.forms import TypesForms, WorkersForms
from Workers.models_workers import Types, Workers


# Widok tworzacy typ pracownika
class TypeFormView(CreateView):
    form_class = TypesForms
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('index')


# Widok listy typów pracy
class TypeWorkListView(View):
    def get(self, request):
        types = Types.objects.all()
        return render(request, 'type_work_list.html', {'types': types})


# Widok tworzący pracownika
class WorkersFormView(CreateView):
    form_class = WorkersForms
    template_name = 'form.html'

    def get_success_url(self):
        return reverse('type_work_list')


# Widok listy pracownikow wzgledem typu pracy
class WorkersListByTypeView(View):
    def get(self, request, id):
        types = Types.objects.get(id=id)
        workers = Workers.objects.filter(type=types)
        return render(request, 'workers_list_by_type.html', {'workers': workers})

# Widok edycji Workers
class WorkersEditView(View):
    def get(self, request, id_t, id):
        types = Types.objects.all()
        workers = Workers.objects.get(id=id)
        return render(request, 'edit_worker.html', {'types':types, 'workers':workers})
    def post(self, request, id_t, id):
        workers = Workers.objects.get(id=id)
        name = request.POST.get('name')
        type_id= request.POST['type']
        types = Types.objects.get(id= type_id)
        price = request.POST.get('price')
        work = request.POST.get('work')
        workers.name = name
        workers.type_id = types
        workers.price = price
        workers.work =work
        workers.save()
        return redirect('type_work_list')