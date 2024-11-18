from django import forms
from.models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'
        widgets={
            'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email ID'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address'}),
            'phonenum': forms.NumberInput(attrs={'placeholder': '+91 xxxxx xxxxx'}),
            'date':forms.DateInput(attrs={'placeholder':"DD/MM/YYYY"}),
            'time':forms.TimeInput(attrs={'placeholder':"HH/MM/SS"}),

        }