from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.reason} - {self.amount}"
    
