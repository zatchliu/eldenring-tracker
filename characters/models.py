from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boss(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    region=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    completed_bosses = models.ManyToManyField(Boss, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Calculate the new level based on the average of all stats
        if not self.pk:
            return super(Character, self).save(*args, **kwargs)
        old_vigor = self.__class__.objects.get(pk=self.pk).vigor
        old_mind = self.__class__.objects.get(pk=self.pk).mind
        old_endurance = self.__class__.objects.get(pk=self.pk).endurance
        old_strength = self.__class__.objects.get(pk=self.pk).strength
        old_dexterity = self.__class__.objects.get(pk=self.pk).dexterity
        old_intelligence = self.__class__.objects.get(pk=self.pk).intelligence
        old_faith = self.__class__.objects.get(pk=self.pk).faith
        old_arcane = self.__class__.objects.get(pk=self.pk).arcane

        stat_diff = ((self.vigor-old_vigor)+
                     (self.mind-old_mind)+
                     (self.endurance-old_endurance)+
                     (self.strength-old_strength)+
                     (self.dexterity-old_dexterity)+
                     (self.intelligence-old_intelligence)+
                     (self.faith-old_faith)+
                     (self.arcane-old_arcane)
                     )
                     
        self.level+=stat_diff

        super(Character, self).save(*args, **kwargs)
