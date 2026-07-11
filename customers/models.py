from django.db import models


class Customer(models.Model):

    name = models.CharField(max_length=150)

    phone = models.CharField(max_length=15)

    email = models.EmailField(blank=True)

    address = models.TextField(blank=True)

    credit_balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name