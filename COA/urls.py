from django.urls import path
from . import views

urlpatterns = [
    path('', views.coa_list, name='coa_list'),
    path('create/', views.coa_create, name='coa_create'),
    path('ajax/load-detail-types/', views.ajax_load_detail_types, name='ajax_load_detail_types'),
]
