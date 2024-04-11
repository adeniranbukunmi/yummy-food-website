from django.db import models

# Create your models here.

class FoodCatalogue(models.Model):
    
    name = models.CharField(max_length=100)   
    img= models.ImageField(upload_to="foodItemGalary")
    description=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)