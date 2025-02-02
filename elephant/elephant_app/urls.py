from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path("add_category", views.add_category, name="add_category"),
    path('add_item', views.add_item, name='add_item'),
]

