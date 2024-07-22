from django import forms

from .models import COA

class COAForm(forms.ModelForm):
    class Meta:
        model = COA
        fields = ['name', 'description', 'account_type', 'detail_type', 'balance']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter name'})

        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter description'})

        self.fields['account_type'].widget.attrs.update({'class': 'form-control', 'id': 'id_account_type'})

        self.fields['detail_type'].widget = forms.Select(
            choices=self.get_detail_type_choices(), 
            attrs={'class': 'form-control', 'id': 'id_detail_type'}
        )

        self.fields['balance'].required = False
        self.fields['balance'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter balance'})
        self.fields['balance'].initial = self.instance.balance or 0  # Set initial value to 0 if None

    def get_detail_type_choices(self):
        account_type = self.initial.get('account_type') or (self.instance.account_type if self.instance else None)
        if account_type:
            return COA.DETAIL_TYPES.get(account_type, [])
        else:
            return []
