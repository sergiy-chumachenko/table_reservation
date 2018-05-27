from django import forms
from datetime import datetime


class OrderForm(forms.Form):
    date_now = datetime.now().date().strftime("%m/%d/%Y")
    order_date = forms.DateField(required=True, label='Order Date',
                                 widget=forms.DateInput(attrs={'class': 'datepicker validate',
                                                               'type': 'text',
                                                               'id': 'date_for',
                                                               'name': 'order_date',
                                                               'value': date_now},
                                                        ))

    table_id = forms.CharField(required=True, label="Table ID",
                               widget=forms.HiddenInput())
    first_name = forms.CharField(required=True, max_length=50,
                                 widget=forms.TextInput(attrs={
                                     'type': 'text',
                                     'name': 'first_name',
                                     'class': "validate"
                                 }))
    last_name = forms.CharField(required=True, max_length=50,
                                widget=forms.TextInput(attrs={

                                    'type': 'text',
                                    'name': 'first_name',
                                    'class': "validate"
                                }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                    'type': 'text',
                                    'name': 'first_name',
                                    'class': "validate"
                                }))
