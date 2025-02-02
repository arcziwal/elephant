from django import forms
from .models import Item, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'stock', 'category']
