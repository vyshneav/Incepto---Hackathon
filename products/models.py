from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
