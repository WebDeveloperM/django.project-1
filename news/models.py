from contextlib import nullcontext
from email.mime import image
from pyexpat import model
from django.db import models

# Create your models here.


# Kurslar modeli
class Course(models.Model):
    name = models.CharField(max_length=200)
    tarif = models.TextField()
    narx = models.IntegerField()
    davomiyligi = models.IntegerField()

    def __str__(self):
        return self.name


# O`qituvchilar uchun model   
class Teacher(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(null=True,)
    teaching_course = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.full_name
