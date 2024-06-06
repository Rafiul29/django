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
  image = models.ImageField(upload_to='posts/images',default='posts/images/default.png', )

  # blank = True, null = True
  def __str__(self) -> str:
    return self.title

  
 
class Comment(models.Model):
  post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
  name=models.CharField(max_length=30)
  email=models.EmailField()
  body=models.TextField()
  created_on=models.DateTimeField(auto_now=True)


  def __str__(self) -> str:
    return f"Comments by {self.name}"
