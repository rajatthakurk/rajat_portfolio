from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.ImageField(upload_to="profile_photo")
    role = models.CharField(max_length = 100)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length = 15)

class Skills(models.Model):
    skill_name = models.CharField(max_length = 100)
    skill_percentage = models.PositiveIntegerField()

class Languages(models.Model):
    language_name = models.CharField(max_length = 50)
    language_percentage = models.FloatField()

class Work_Experience(models.Model):
    company_name = models.CharField(max_length = 100)
    designation = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def clean(self):
        super().clean()
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError(_('End date cannot be before start date'))


class Education(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    degree_name = models.CharField(max_length=200)

    def clean(self):
        super().clean()
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError(_('End date cannot be before start date'))