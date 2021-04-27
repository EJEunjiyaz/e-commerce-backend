from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=256)
    url = models.URLField(max_length=512)
    datetime_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProductQuery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    rating_person = models.PositiveIntegerField()
    sold = models.PositiveIntegerField()
    datetime_query = models.DateTimeField(auto_now_add=True)
