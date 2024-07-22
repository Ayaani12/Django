# forms.py

from django import forms
from .models import *
from Journal_Entries.models import *

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'city', 'country', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SalesPersonForm(forms.ModelForm):
    class Meta:
        model = SalesPerson
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'country', 'store']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'rate', 'duration', 'store']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'store': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'  # You can specify specific fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter phone number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter address'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter city'})
        self.fields['state'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter state'})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter country'})
        self.fields['postal_code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter postal code'})
        self.fields['store'].widget.attrs.update({'class':'form-control','placeholder':'Enter Store'})


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'  # You can specify specific fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter phone number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter address'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter city'})
        self.fields['state'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter state'})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter country'})
        self.fields['postal_code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter postal code'})
        self.fields['store'].widget.attrs.update({'class':'form-control','placeholder':'Enter Store'})


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'  # You can specify specific fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize form field attributes if needed
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter last name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter phone number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter address'})
        self.fields['city'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter city'})
        self.fields['state'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter state'})
        self.fields['country'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter country'})
        self.fields['postal_code'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter postal code'})
        self.fields['store'].widget.attrs.update({'class':'form-control','placeholder':'Enter Store'})

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  # You can specify specific fields if needed

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize form field attributes if needed
        self.fields['project_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter project name'})