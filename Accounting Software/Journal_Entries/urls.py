from django.urls import path
from .views import create_journal_entry

urlpatterns = [
    path('create/', create_journal_entry, name='create_journal_entry'),
]