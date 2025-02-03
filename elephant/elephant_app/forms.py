from django import forms
from .models import Item, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Nazwa Kategorii'
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'stock', 'category']
        labels = {
            'name': 'Nazwa Produktu',
            'description': 'Opis',
            'price': 'Cena brutto',
            'stock': 'Ilość dostępnych sztuk',
            'category': 'Kategoria'
        }