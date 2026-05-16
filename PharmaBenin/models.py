from django.db import models

class Pharmacy(models.Model):
    name = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name