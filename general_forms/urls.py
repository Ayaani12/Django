from django.urls import path
from .views import *

urlpatterns = [
    path('store',store,name="store"),
    path('Seller',seller,name='seller'),
    path('Product',product,name='product'),
    path('Service',service,name='service'),
    path('Customer',customer,name='customer'),
    path('Vendor',vendor,name='vendor'),
    path('Employee',employee,name='employee'),
    path('Project',project,name='project')

]