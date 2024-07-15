from django.db import models

class Monitoring(models.Model):
    monitoring_date = models.DateField()
    monitor_name = models.CharField(max_length=200)
    monitor_id = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

class CropPlantInfo(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    crop_plant_type = models.CharField(max_length=200)
    variety = models.CharField(max_length=200)
    growth_stage = models.CharField(max_length=200)

class PestMonitoringData(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    pest_presence = models.BooleanField()
    pest_type = models.CharField(max_length=200)
    pest_name = models.CharField(max_length=200)
    pest_density = models.IntegerField()
    pest_damage = models.TextField()
    pest_life_stage = models.CharField(max_length=200)

class DiseaseMonitoringData(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    disease_presence = models.BooleanField()
    disease_type = models.CharField(max_length=200)
    disease_name = models.CharField(max_length=200)
    disease_severity = models.CharField(max_length=200)
    disease_symptoms = models.TextField()
    disease_spread = models.CharField(max_length=200)
    disease_incidence = models.FloatField()

class EnvironmentalCondition(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    soil_moisture = models.FloatField()
    weather_conditions = models.CharField(max_length=200)

class ManagementPractice(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    current_practices = models.TextField()
    effectiveness = models.CharField(max_length=200)
    new_measures = models.TextField()

class DataCollectionTool(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    traps_used = models.CharField(max_length=200)
    sensors_deployed = models.CharField(max_length=200)
    survey_methods = models.CharField(max_length=200)

class AttachmentMedia(models.Model):
    monitoring = models.ForeignKey(Monitoring, on_delete=models.CASCADE)
    photo_video = models.FileField(upload_to='attachments/')
    notes = models.TextField()
