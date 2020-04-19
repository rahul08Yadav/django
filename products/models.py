from django.db import models


# Create your models here.




class Product(models.Model):
    name= models.CharField(max_length=255,null=True,blank=True)
    price = models.FloatField(null=True,blank=True)
    rating = models.CharField(max_length=4,null=True,blank=True)
    rest_address = models.CharField(max_length=2083,null=True,blank=True)
    image_url = models.CharField(max_length=2083,null=True)
    location = models.CharField(max_length=127,null=True,blank=True)
    cuisines = models.CharField(max_length=127,null=True,blank=True)
    timings_and_perks = models.CharField(max_length=2000,null=True,blank=True)
    res_url = models.CharField(max_length=2083,null=True)
    votes = models.CharField(max_length=100,null=True,blank=True)







class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()



