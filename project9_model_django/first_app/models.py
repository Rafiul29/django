from django.db import models

# Create your models here.
class Student(models.Model):
  name=models.CharField(max_length=20)
  roll=models.IntegerField(primary_key=True)
  address=models.TextField()
  father_name=models.TextField(default='ra')

  def __str__(self):
    return f"Roll : {self.roll}-{self.name}"


class StudentModel(models.Model):
  roll=models.IntegerField(primary_key=True)
  name=models.CharField(max_length=20)
  father_name=models.CharField(max_length=30)
  address=models.TextField()

