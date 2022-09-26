from django import forms
from .models import Laptop

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields='__all__'
        labels={
            'lname':'LAPTOP NAME',
            'cname':'COMPANY NAME',
            'ram':' RAM',
            'rom':'ROM',
            'price':'PRICE',
            'processor':'PROCESSOR'
        }
        widgets={
            'lname':forms.TextInput(attrs={'placeholder':'eg.shoes'}),

        }