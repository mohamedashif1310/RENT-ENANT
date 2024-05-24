from django.db import models

# Create your models here.
from django.db import models
from users.models import CustomUser

class Property(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    nearby_amenities = models.TextField()

    def __str__(self):
        return self.title
