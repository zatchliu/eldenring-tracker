from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0)
    class_name = models.CharField(max_length=50)
    vigor=models.IntegerField(default=0)
    mind=models.IntegerField(default=0)
    endurance=models.IntegerField(default=0)
    strength=models.IntegerField(default=0)
    dexterity=models.IntegerField(default=0)
    intelligence=models.IntegerField(default=0)
    faith=models.IntegerField(default=0)
    arcane=models.IntegerField(default=0)
