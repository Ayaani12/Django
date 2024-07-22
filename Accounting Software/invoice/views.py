from django.shortcuts import render, redirect
from .forms import InvoiceEntryForm, InvoiceEntryLineProductFormSet
from .models import InvoiceEntry

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceEntryForm(request.POST)
        formset = InvoiceEntryLineProductFormSet(request.POST, instance=form.instance)
        
        if form.is_valid() and formset.is_valid():
            # Save the invoice entry first
            invoice = form.save(commit=False)
            
            # Calculate total_amount and grand_total_taxed
            total_amount = 0
            grand_total_taxed = 0
            for line_form in formset:
                if line_form.is_valid():  # Check if individual forms in formset are valid
                    amount_before_tax = line_form.cleaned_data.get('amount_before_tax', 0)
                    amount_after_tax = line_form.cleaned_data.get('amount_after_tax', 0)
                    total_amount += float(amount_before_tax)
                    grand_total_taxed += float(amount_after_tax)
            
            invoice.total_amount = total_amount
            invoice.grand_total_taxed = grand_total_taxed
            invoice.save()
            
            # Save each line product
            formset.instance = invoice  # Set the formset instance to the saved invoice
            formset.save()  # Save formset with the correct instance
            
            return redirect('create_invoice')  # Redirect to a success page or another view
    else:
        form = InvoiceEntryForm()
        formset = InvoiceEntryLineProductFormSet()
    
    return render(request, 'create_invoice_entry.html', {
        'form': form,
        'formset': formset
    })
