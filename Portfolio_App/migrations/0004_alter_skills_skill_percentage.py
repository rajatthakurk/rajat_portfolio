# Generated by Django 4.2.11 on 2024-03-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio_App', '0003_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skill_percentage',
            field=models.PositiveIntegerField(),
        ),
    ]
