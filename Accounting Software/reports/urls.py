from django.urls import path
from .views import *

urlpatterns = [
    path('', reports, name='reports'),
    
]
