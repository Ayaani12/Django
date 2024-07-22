from django.shortcuts import render, redirect
from .forms import JournalEntriesForm, JournalEntryLinesFormSet
from .models import JournalEntries

def create_journal_entry(request):
    if request.method == 'POST':
        form = JournalEntriesForm(request.POST)
        formset = JournalEntryLinesFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.save()

            for form in formset:
                if form.cleaned_data.get('account'):  # Assuming account is required
                    journal_entry_line = form.save(commit=False)
                    combined_selection = form.cleaned_data.get('combined_selection')
                    
                    if combined_selection:
                        type, id = combined_selection.split('-')
                        
                        if type == 'customer':
                            journal_entry_line.customer_id = id
                        elif type == 'vendor':
                            journal_entry_line.vendor_id = id
                        elif type == 'employee':
                            journal_entry_line.employee_id = id
                    
                    journal_entry_line.journal_entry = journal_entry  # Linking to the main journal entry
                    journal_entry_line.save()

            return redirect('/JEcreate')  # Replace with your success URL
        else:
            # Clean up formset errors to prevent saving
            formset = JournalEntryLinesFormSet()  # Reset formset to display errors in template
    else:
        form = JournalEntriesForm()
        formset = JournalEntryLinesFormSet()

    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'Journal_Entries.html', context)
