from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.FloatField()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    # if a Brand has multiple Category objects – that is, a Category can be on multiple brands and
    # each Brand has multiple Category
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_code = models.IntegerField()
    title = models.CharField(max_length=200)
    size = models.CharField(max_length=5, choices=[("S", "Small"), ("M", "Medium"), ("L", "Large")])
    price = models.FloatField()
    description = models.CharField(max_length=500)
    states = [("Running out", "Running out"), ("Sold out", "Sold out"), ("Available", "Available")]
    state = models.CharField(max_length=20, choices=states)

    # max 100 stocks, min 0 in stocks
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    # if a Product has multiple Category objects – that is, a Category can be on multiple products and
    # each Product has multiple Category
    category = models.ManyToManyField(Category)

    # if a Product model has a Brand that is, a Brand makes multiple products but each
    # Product only has one Brand
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.title