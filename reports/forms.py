from django import forms
from COA.models import COA  # Import COA model from your COA app

class ReportsForm(forms.Form):
    coa_name = forms.ModelChoiceField(queryset=COA.objects.all(), empty_label="Select COA")
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
