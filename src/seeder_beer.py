from django.db import models


##roduct model

class Category(models.Model):
    pass


class Price(models.Model):
    sum = models.IntegerField()


class Unity(models.Model):
    pass


class AbstractProduct(models.Model):
    category = models.ForeignKey(Category)


class Product(models.Model):
    abstract_product = models.ForeignKey(AbstractProduct)


class Recpvery(models.Model):
    pass


## Transaction model

class Transaction(models.Model):
    product = models.ForeignKey(Product)
