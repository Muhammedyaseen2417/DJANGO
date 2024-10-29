from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField()
    roll_num=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
