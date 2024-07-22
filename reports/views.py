from django.shortcuts import render
from .forms import ReportsForm
from Journal_Entries.models import *
from COA.models import COA


def reports(request):
    form = ReportsForm(request.POST or None)
    report_data = None
    
    if request.method == 'POST':
        if form.is_valid():
            coa_name = form.cleaned_data['coa_name']
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']
            
            # Fetch JournalEntryLines filtered by COA ID and date range
            journal_entry_lines = JournalEntryLines.objects.filter(
                account=coa_name,
                journal_entry__date__range=[from_date, to_date]
            ).select_related('journal_entry', 'customer', 'vendor', 'employee', 'project')
            
            # Prepare report data
            report_data = []
            for line in journal_entry_lines:
                entry_data = {
                    'date': line.journal_entry.date,
                    'reference': line.journal_entry.reference,
                    'name': '',  # Placeholder for name
                    'description': line.description,
                    'debit': line.debit,
                    'credit': line.credit,
                    'project_name': line.project.project_name if line.project else ''
                }
                
                # Determine the name based on the related model
                if line.customer:
                    entry_data['name'] = line.customer.name
                elif line.vendor:
                    entry_data['name'] = line.vendor.name
                elif line.employee:
                    entry_data['name'] = f"{line.employee.first_name} {line.employee.last_name}"
                
                report_data.append(entry_data)
    
    context = {
        'form': form,
        'report_data': report_data,
    }
    return render(request, 'reports.html', context)
