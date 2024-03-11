from django.contrib import admin
from .models import Profile, Skills, Languages, Work_Experience, Education

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'phone')
    search_fields = ('name', 'role', 'email')

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_percentage')

@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('language_name', 'language_percentage')

@admin.register(Work_Experience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('designation', 'start_date', 'end_date', 'description')
    list_filter = ('designation', 'start_date', 'end_date')
    search_fields = ('designation', 'description')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'degree_name')
    list_filter = ('degree_name', 'start_date', 'end_date')
    search_fields = ('name', 'degree_name')
