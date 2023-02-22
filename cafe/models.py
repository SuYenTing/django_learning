from django.db import models

class Product(models.Model):

    SIZES={
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    }

    pid=models.CharField(max_length=5)
    name=models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    size=models.CharField(max_length=1, choices=SIZES)