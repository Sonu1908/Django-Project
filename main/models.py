
from django.db import models



# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    


class Professor(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return self.name











  
