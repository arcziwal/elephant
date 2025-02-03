from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CategoryForm, ItemForm
from .models import Category, Item

def hello_world(request):
    return render(request, 'HelloWorld.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'new_category.html', {'form': form})

def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'new_item.html', {'form': form})

def list_items(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def home_page(request):
    return render(request, 'home.html')
