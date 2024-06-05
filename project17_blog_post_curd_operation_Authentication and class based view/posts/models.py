from django.db import models
from categories.models import Category
# from author.models import Author
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title=models.CharField(max_length=50)
  content=models.TextField()
  category=models.ManyToManyField(Category) #many to many relationships
  author=models.ForeignKey(User,on_delete=models.CASCADE) #many to one  or one to many relationships
  
  def __str__(self) -> str:
    return self.title

  
 
