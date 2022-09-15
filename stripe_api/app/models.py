from django.db import models

class Item(models.Model):

    name = models.CharField(max_length=100, verbose_name='Наименование')
    stripe_product_id = models.CharField(max_length=100)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name



class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_display_price(self):
        return self.price