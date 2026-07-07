# Uncomment the following imports before adding the Model code

from django.db import models

# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("WAGON", "Wagon"),
        ("HATCHBACK", "Hatchback"),
        ("COUPE", "Coupe"),
        ("CONVERTIBLE", "Convertible"),
    ]

    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="car_models"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.IntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
