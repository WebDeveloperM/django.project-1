from django.shortcuts import render

from news.models import Course, Teacher

# Create your views here.


# home funksiyasi

def home(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    return render(request, 'home.html', {'kurslar': courses, 'teachers': teachers })

# about_detail funksiyasi
def about_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'about_detail.html', {'course': course})

