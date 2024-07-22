from django.db import models
from django.core.validators import MinValueValidator
from general_forms.models import *

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.pk})"

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)




    def __str__(self):
        return f"{self.name} ({self.pk})"

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.pk})"

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.project_name} ({self.id})"

from django.db import models
from COA.models import COA  # Importing COA model from COA app

class JournalEntries(models.Model):
    journal_entry_id = models.AutoField(primary_key=True)
    date = models.DateField()
    reference = models.CharField(max_length=255, blank=True, null=True)
    posted = models.BooleanField(default=False)

    def __str__(self):
        return f"Journal Entry ID: {self.journal_entry_id}"




class JournalEntryLines(models.Model):
    journal_entry_line_id = models.AutoField(primary_key=True)
    journal_entry = models.ForeignKey(JournalEntries, on_delete=models.CASCADE)
    account = models.ForeignKey(COA, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    debit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True, related_name='customer_lines')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True, related_name='vendor_lines')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, related_name='employee_lines')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Journal Entry Line ID: {self.journal_entry_line_id}"
