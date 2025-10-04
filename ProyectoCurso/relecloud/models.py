from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
    unique=True, 
    null=False,
    blank=False,
    max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    duration = models.IntegerField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False
    )
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
class InfoRequest(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=50
    )
    email = models.EmailField(
        null=False,
        blank=False,
        max_length=254
    )
   