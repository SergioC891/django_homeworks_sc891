from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)


class Measurement(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(null=True, blank=True)

