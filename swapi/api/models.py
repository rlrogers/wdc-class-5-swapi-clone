from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField(null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)


class People(models.Model):
    HAIR_COLOR_CHOICES = (
        ('blond', 'Blond'),
        ('black', 'Black'),
        ('brown', 'Brown'),
        ('red', 'Red'),
    )
    name = models.CharField(max_length=255)
    homeworld = models.ForeignKey(Planet, on_delete=models.CASCADE)
    height = models.IntegerField(null=True, blank=True)
    mass = models.IntegerField(null=True, blank=True)
    hair_color = models.CharField(
        max_length=10, choices=HAIR_COLOR_CHOICES, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
