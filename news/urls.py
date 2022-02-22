
from django.urls import path
from news.views import home, about_detail

urlpatterns = [
    path('', home, name='home'),
    path('about_detail/<int:pk>', about_detail, name="about_detail")
]

