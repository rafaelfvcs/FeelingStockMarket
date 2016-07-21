from __future__ import unicode_literals

from django.db import models

# 
class Stock(models.Model):
    company = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    country = models.CharField(max_length=85)
    company_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.company+' <-> '+self.symbol
    
class Prices(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE) # se del Stock Price vai junto
    prices_type = models.CharField(max_length=20)
    values = models.DecimalField(max_digits=20,decimal_places=4)
    def __str__(self):
            return self.stock+' <-> '+self.prices_type

