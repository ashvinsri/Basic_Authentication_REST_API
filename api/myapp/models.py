from django.db import models

# Create your models here.

class Student(models.Model):
    rollno=models.CharField(max_length=264,unique=True)
    name=models.CharField(max_length=264)
    city=models.CharField(max_length=264)

    def __str__(self):
        return self.name

