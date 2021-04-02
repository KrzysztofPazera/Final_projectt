"""WycenaSzkody URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Car_Base import views
from Workers import views_workers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('add_car_brand/', views.CarBrandFormView.as_view(), name = 'add_car_brand'),
    path('car_brand_list/', views.CarBrandListView.as_view(), name = 'car_brand_list'),
    path('add_car_model/', views.AddCarModelFormView.as_view(), name='add_car_model'),
    path('car_brand_list/car_models/<int:id>/', views.CarModelListView.as_view(), name='car_list_by_brand'),
    path('add_parts_category/', views.PartsCategoyFormView.as_view(), name='add_category_of_parts'),
    path('add_part/', views.CarPartsFormView.as_view(),name='add_car_part'),
    path('parts_category_list/', views.PartsCategoryListView.as_view(), name='parts_category'),
    path('parts_category_list/parts_list/<int:id>/', views.PartsListView.as_view(), name= 'parts_list'),
    path('parts_category_list/parts_list/<int:id_c>/<int:id>/', views.PartsDetailView.as_view(), name='part_detail'),
    path('parts_category_list/parts_list/<int:id_c>/<int:id>/edit_part/', views.PartsDetailEditeView.as_view(), name='part_edit/'),
    path('car_brand_list/car_models/<int:id_m>/<int:id>/', views.CarDetailView.as_view(),
         name='part_edit/'),
    path('car_brand_list/car_models/<int:id_m>/<int:id>/edit_car/', views.CarEditView.as_view(), name = 'car_edit'),
    path('add_type_work/', views_workers.TypeFormView.as_view(), name='add_type_work'),
    path('type_work_list/', views_workers.TypeWorkListView.as_view(), name='type_work_list'),
    path('add_workers/', views_workers.WorkersFormView.as_view(), name='add_worker'),
    path('type_work_list/<int:id>/', views_workers.WorkersListByTypeView.as_view(), name='worker_list_by_type'),
    path('type_work_list/<int:id_t>/<int:id>/edit_work/', views_workers.WorkersEditView.as_view(), name='worker_edit'),

]
