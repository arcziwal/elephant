from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa kategorii')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nazwa produktu')
    description = models.TextField(verbose_name='Opis')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cena')
    stock = models.IntegerField(verbose_name="Dostępna ilość")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategoria')

    def __str__(self):
        return self.name
