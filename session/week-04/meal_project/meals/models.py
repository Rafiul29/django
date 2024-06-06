from django.db import models

# Create your models here.
class Category(models.Model):
  category_name=models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.category_name

class Food(models.Model):
  food_name=models.CharField(max_length=250)
  food_description=models.TextField()
  category=models.ForeignKey(Category,on_delete=models.CASCADE)
  image=models.ImageField(upload_to='meals/images' ,default='meals/images/default.png')

  def __str__(self) -> str:
    return self.food_name
