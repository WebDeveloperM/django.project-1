from django.shortcuts import render

from news.models import Course

# Create your views here.


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'kurslar': courses})



