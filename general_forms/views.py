# views.py

from django.shortcuts import render, redirect
from .forms import *

def store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')  
    else:
        form = StoreForm()

    return render(request, 'store.html', {'form': form})


def seller(request):
    if request.method == 'POST':
        form = SalesPersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('seller')  
    else:
        form = SalesPersonForm()

    return render(request, 'salesperson.html', {'form': form})


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')  # Replace 'product_list' with your URL name for product list view or homepage
    else:
        form = ProductForm()

    return render(request, 'product.html', {'form': form})

def service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service')  # Replace 'service_list' with your URL name for service list view or homepage
    else:
        form = ServiceForm()

    return render(request, 'service.html', {'form': form})


def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')  # Replace 'customer_list' with your URL name for customer list view or homepage
    else:
        form = CustomerForm()

    return render(request, 'customer.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import VendorForm

def vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor')  # Replace 'vendor_list' with your actual URL name for vendor listing
    else:
        form = VendorForm()
    
    return render(request, 'vendor.html', {'form': form})

def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another URL
            return redirect('employee')  # Replace with your desired URL name
    else:
        form = EmployeeForm()
    
    return render(request, 'employee.html', {'form': form})

def project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another URL
            return redirect('project')  # Replace with your desired URL name
    else:
        form = ProjectForm()
    
    return render(request, 'project.html', {'form': form})