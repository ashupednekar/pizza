from django.db import models

class OrderHist(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    pizza = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)