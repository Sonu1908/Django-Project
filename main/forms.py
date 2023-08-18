
from django import forms
from .models import Professor


class ProductForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'



        