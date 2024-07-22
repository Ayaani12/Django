from django import forms
from .models import InvoiceEntry, InvoiceEntryLineProduct

class InvoiceEntryForm(forms.ModelForm):
    class Meta:
        
        model = InvoiceEntry
        fields = ['invoice_date', 'due_date', 'customer', 'project', 'status','total_amount', 'paid_amount', 'grand_total_taxed']
        widgets = {
            'invoice_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'total_amount': forms.TextInput(attrs={'readonly':'readonly'}),
            'paid_amount': forms.TextInput(attrs={}),
            'grand_total_taxed': forms.TextInput(attrs={'readonly':'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['invoice_date'].widget.attrs.update({'type': 'date'})
        

class InvoiceEntryLineProductForm(forms.ModelForm):
    class Meta:
        model = InvoiceEntryLineProduct
        fields = ['product', 'description', 'quantity', 'unit_price', 'amount_before_tax', 'taxable', 'gst_percentage', 'amount_after_tax']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['unit_price'].widget.attrs.update({'readonly': 'readonly'})
        self.fields['amount_before_tax'].widget.attrs.update({'readonly': 'readonly'})
        self.fields['amount_after_tax'].widget.attrs.update({'readonly': 'readonly'})


from django.forms import inlineformset_factory


# Formset for InvoiceEntryLineProduct
InvoiceEntryLineProductFormSet = inlineformset_factory(
    InvoiceEntry,
    InvoiceEntryLineProduct,
    form=InvoiceEntryLineProductForm,
    extra=50,  # Total number of forms available
    can_delete=True  # Allow deletion of forms
)
