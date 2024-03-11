from django.shortcuts import render
from .models import Profile,Work_Experience,Education,Skills,Languages

# Create your views here.
def portfolio(request):
    profiles = Profile.objects.all().order_by('-id')
    work = Work_Experience.objects.all().order_by('-id')
    education = Education.objects.all().order_by('-id')
    skills = Skills.objects.all()
    languages = Languages.objects.all()

    context = {
        'profiles' : profiles,
        'work' : work,
        'education' : education,
        'skills' : skills,
        'languages' : languages
    }

    return render(request,'index.html',context)