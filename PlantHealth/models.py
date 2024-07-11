from django.db import models
from django.utils import timezone

class Permit(models.Model):
    customer_name = models.CharField(max_length=200)
    inspector = models.CharField(max_length=200)
    disease_identified = models.CharField(max_length=200)
    region_of_origin = models.CharField(max_length=200)
    country_heading = models.CharField(max_length=200)
    quantity = models.FloatField()
    test_conducted = models.CharField(max_length=200)
    chemical_used = models.CharField(max_length=200)
    volume_used = models.FloatField()
    total_charge = models.FloatField()
    station = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=[('Pass', 'Pass'), ('Rejected', 'Rejected')])
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer_name} - {self.id}'


class User(models.Model):
    name = models.CharField(max_length=200)
    highest_education_level = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    inspection_station = models.CharField(max_length=200)
    certifications = models.TextField()

    def __str__(self):
        return self.name
