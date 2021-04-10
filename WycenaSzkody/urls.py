
from django.contrib import admin
from django.urls import path

from Car_Base import views
from Repair_estimate import views_repair_estimate
from Workers import views_workers
from Account import views_account

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add_car_brand/', views.CarBrandFormView.as_view(), name='add_car_brand'),
    path('car_brand_list/', views.CarBrandListView.as_view(), name='car_brand_list'),
    path('delete_brand/<int:id>', views.delete_car_brand, name='delete_car_brand'),
    path('delete_model/<int:id>', views.delete_car_model, name='delete_car_model'),
    path('delete_category/<int:id>', views.delete_part_category, name='delete_car_category'),
    path('delete_part/<int:id>', views.delete_part, name='delete_car_part'),
    path('add_car_model/', views.AddCarModelFormView.as_view(), name='add_car_model'),
    path('car_brand_list/car_models/<int:id>/', views.CarModelListView.as_view(), name='car_list_by_brand'),
    path('add_parts_category/', views.PartsCategoyFormView.as_view(), name='add_category_of_parts'),
    path('add_part/', views.CarPartsFormView.as_view(), name='add_car_part'),
    path('parts_category_list/', views.PartsCategoryListView.as_view(), name='parts_category'),
    path('parts_category_list/parts_list/<int:id>/', views.PartsListView.as_view(), name='parts_list'),
    path('parts_category_list/parts_list/<int:id_c>/<int:id>/', views.PartsDetailView.as_view(), name='part_detail'),
    path('parts_category_list/parts_list/<int:id_c>/<int:id>/edit_part/', views.PartsDetailEditeView.as_view(),
         name='part_edit/'),
    path('car_brand_list/car_models/<int:id_m>/<int:id>/', views.CarDetailView.as_view(),
         name='part_edit/'),
    path('car_brand_list/car_models/<int:id_m>/<int:id>/edit_car/', views.CarEditView.as_view(), name='car_edit'),
    path('add_type_work/', views_workers.TypeFormView.as_view(), name='add_type_work'),
    path('type_work_list/', views_workers.TypeWorkListView.as_view(), name='type_work_list'),
    path('add_workers/', views_workers.WorkersFormView.as_view(), name='add_worker'),
    path('type_work_list/<int:id>/', views_workers.WorkersListByTypeView.as_view(), name='worker_list_by_type'),
    path('type_work_list/<int:id_t>/<int:id>/edit_work/', views_workers.WorkersEditView.as_view(), name='worker_edit'),
    path('car_filter/', views_repair_estimate.car_filter_view, name='car_filter'),
    path('repair_list/', views_repair_estimate.repair_list_view, name='repair_list'),
    path('add_client_form/', views_repair_estimate.AddClientView.as_view(), name='add_client_view'),
    path('add_to_cart/<int:id>/', views_repair_estimate.add_to_cart_view, name="add_to_cart"),
    path('set_cleint/', views_repair_estimate.set_client, name='set_client'),
    path('add_client/<int:id>/', views_repair_estimate.add_client, name='add_client'),
    path('products_list/', views_repair_estimate.sumary_list, name='sumary_list'),
    path('delete/<int:id>/', views_repair_estimate.delete_full_from_list, name='delete_item'),
    path('delete_one/<int:id>/', views_repair_estimate.delete_from_list, name='delete_one_item'),
    path('updata_one/<int:id>/', views_repair_estimate.updata_in_list, name='updata_list'),
    path('login/', views_account.LoginView.as_view(), name='login'),
    path('logout/', views_account.LogOutView.as_view(), name='logout'),
    path('register/', views_account.RegisterView.as_view(), name='register'),
    path('add_parts_works/', views.AddPartsAndWorkFormView.as_view(), name='add_parts_works'),
    path('parts_works_list/', views.PartsAndWorksListView.as_view(), name='parts_works_list'),

]

