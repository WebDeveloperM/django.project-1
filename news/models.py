from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)
    tarif = models.TextField()
    narx = models.IntegerField()
    davomiyligi = models.IntegerField()

    def __str__(self):
        return self.name
        