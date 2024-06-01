from django.db import models
from categories.models import Category


# Create your models here.
class Task(models.Model):
  title=models.CharField(max_length=150)
  description=models.TextField()
  category=models.ManyToManyField(Category) #many to many relation ships
  date=models.DateField()
  is_complete=models.BooleanField()

  def __str__(self) -> str:
    return self.title