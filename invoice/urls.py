from django.urls import path
from .views import *

urlpatterns = [
    path('invoice/create',create_invoice,name='create_invoice'),


]
