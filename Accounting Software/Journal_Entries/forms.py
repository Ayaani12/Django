from django import forms
from .models import JournalEntries, JournalEntryLines, Customer, Vendor, Employee, Project
from django.forms import inlineformset_factory  # Import inlineformset_factory

class JournalEntriesForm(forms.ModelForm):
    class Meta:
        model = JournalEntries
        fields = ['date', 'reference', 'posted']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'id': 'date-id'}),
            'reference': forms.TextInput(attrs={'id': 'reference-id'}),
            'posted': forms.CheckboxInput(attrs={'id': 'posted-id'}),
        }

class JournalEntryLinesForm(forms.ModelForm):
    combined_selection = forms.ChoiceField(widget=forms.Select(attrs={'id': 'combined-selection-id', 'class': 'form-control-plaintext'}))

    class Meta:
        model = JournalEntryLines
        fields = ['account', 'description', 'debit', 'credit', 'project']
        widgets = {
            'account': forms.Select(attrs={'id': 'account-id', 'class': 'form-control-plaintext'}),
            'description': forms.TextInput(attrs={'id': 'description-id', 'class': 'form-control-plaintext'}),
            'debit': forms.NumberInput(attrs={'id': 'debit-id', 'class': 'form-control-plaintext'}),
            'credit': forms.NumberInput(attrs={'id': 'credit-id', 'class': 'form-control-plaintext'}),
            'project': forms.Select(attrs={'id': 'project-id', 'class': 'form-control-plaintext'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(JournalEntryLinesForm, self).__init__(*args, **kwargs)
        customers = Customer.objects.all()
        vendors = Vendor.objects.all()
        employees = Employee.objects.all()

        choices = [
            ('', 'Select Name'),
        ]
        
        for customer in customers:
            choices.append((f'customer-{customer.id}', f'{customer.name}'))

        for vendor in vendors:
            choices.append((f'vendor-{vendor.id}', f'{vendor.name}'))

        for employee in employees:
            choices.append((f'employee-{employee.id}', f'{employee.first_name} {employee.last_name}'))

        self.fields['combined_selection'].choices = choices

    def clean(self):
        cleaned_data = super().clean()
        debit = cleaned_data.get('debit')
        credit = cleaned_data.get('credit')

        if debit is None and credit is None:
            raise forms.ValidationError("You must enter either a debit or a credit.")

        if debit is not None and credit is not None:
            raise forms.ValidationError("You cannot enter both a debit and a credit.")

        return cleaned_data

# Define your formset factory here
JournalEntryLinesFormSet = inlineformset_factory(
    JournalEntries,
    JournalEntryLines,
    form=JournalEntryLinesForm,
    extra=100,
    can_delete=False
)
