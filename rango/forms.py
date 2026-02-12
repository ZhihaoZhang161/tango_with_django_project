from django import forms
from rango.models import Category

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")

    class Meta:
        model = Category
        fields = ('name',)
