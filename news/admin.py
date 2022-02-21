from django.contrib import admin

from news.models import Course, News

# Register your models here.

admin.site.register(Course)
admin.site.register(News)