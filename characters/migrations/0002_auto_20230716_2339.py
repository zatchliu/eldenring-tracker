# Generated by Django 3.2.12 on 2023-07-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='arcane',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='dexterity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='endurance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='faith',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='mind',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='strength',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='vigor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]