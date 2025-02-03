from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path("categories/add", views.add_category, name="add_category"),
    path('items/add', views.add_item, name='add_item'),
    path('categories/list', views.list_categories, name='category_list'),
    path('items/list', views.list_items, name='item_list'),
]

