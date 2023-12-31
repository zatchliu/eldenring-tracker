# Generated by Django 4.2.3 on 2023-07-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20230716_2339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='completed_bosses',
            field=models.ManyToManyField(blank=True, to='characters.boss'),
        ),
    ]
