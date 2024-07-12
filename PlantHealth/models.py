from django.db import models
from django.utils import timezone

class Permit(models.Model):
    customer_name = models.CharField(max_length=200, default='Unknown Customer')  # Set a default value here
    customer_phone = models.IntegerField(default=0)  # Set a default value here
    customer_email = models.EmailField(default='unknown@example.com')  # Set a default value here
    product_name = models.CharField(max_length=200, default='Unknown Product')  # Set a default value here
    inspector = models.CharField(max_length=200, default='Unknown Inspector')  # Set a default value here
    disease_identified = models.CharField(max_length=200, default='None')  # Set a default value here
    region_of_origin = models.CharField(max_length=200, default='Unknown Region')  # Set a default value here
    country_heading = models.CharField(max_length=200, default='Unknown Country')  # Set a default value here
    quantity = models.FloatField(default=0.0)  # Set a default value here
    test_conducted = models.CharField(max_length=200, default='None')  # Set a default value here
    chemical_used = models.CharField(max_length=200, default='None')  # Set a default value here
    volume_used = models.FloatField(default=0.0)  # Set a default value here
    total_charge = models.FloatField(default=0.0)  # Set a default value here
    station = models.CharField(max_length=200, default='Unknown Station')  # Set a default value here
    status = models.CharField(max_length=10, choices=[('Pass', 'Pass'), ('Rejected', 'Rejected')], default='Pass')  # Set a default value here
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.customer_name} - {self.id}'


class User(models.Model):
    name = models.CharField(max_length=200, default='Unknown User')  # Set a default value here
    phone = models.IntegerField(default=0)  # Set a default value here
    email = models.EmailField(default='unknown@example.com')  # Set a default value here
    highest_education_level = models.CharField(max_length=200, default='Unknown')  # Set a default value here
    date_of_birth = models.DateField()
    inspection_station = models.CharField(max_length=200, default='Unknown Station')  # Set a default value here
    certifications = models.TextField(default='None')  # Set a default value here

    def __str__(self):
        return self.name
