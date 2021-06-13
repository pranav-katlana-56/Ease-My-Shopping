from django.db import models
from django import forms

OS = ["Android" , "IOS"]

class Mobile(models.Model):
    Name = models.CharField(max_length=122)
    Price =models.IntegerField()
    Price_flipkart= models.CharField(max_length=10000, default=20000 )
    Price_Amazon = models.CharField(max_length=12435, default="10,000")
    icon = models.CharField(max_length=10000, default="/static/oppo.jpg")
    Brand = models.CharField(max_length=100)
    origin = models.CharField(max_length=122 , default="Made in India")
    category = models.CharField(max_length=122 , default="Android")
    img1 = models.CharField(max_length=2600)
    img2 = models.CharField(max_length=2600)
    img3 = models.CharField(max_length=2600)
    Description = models.CharField(max_length=2000)
    GSM = models.IntegerField()
    kyg = models.IntegerField()
    gadgets = models.IntegerField()
    youtube = models.CharField(max_length=2600)
    Amazon_Link = models.CharField(max_length=3000, default="amazon")
    Flipkart_Link = models.CharField(max_length=3000, default="flipkart")
    
    def __str__(self):
        return self.Name
        
    
    
    



class Gadgets(models.Model):
    Name = models.CharField(max_length=199)
    Price = models.CharField(max_length=199)
    Brand = models.CharField(max_length=199)
    Description = models.CharField(max_length=19999)
    Origin = models.CharField(max_length=199)
    icon = models.CharField(max_length=199, default="/static/")
    img1 = models.CharField(max_length=199)
    img2 = models.CharField(max_length=199)
    img3 = models.CharField(max_length=199)
    youtube = models.CharField(max_length=199)

class Cashback(models.Model):
    Buyer_Name = models.CharField(max_length=200)
    Mobile = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Product_Name = models.CharField(max_length=200)
    Purchase_Value= models.CharField(max_length=200)
    Date_of_Purchase= models.CharField(max_length=200)
    order_id= models.CharField(max_length=200)
    Platform = models.CharField(max_length=200)
    Upi = models.CharField(max_length=200) 
    def __str__(self):
        return self.Buyer_Name 


class Contact(models.Model):
    Name = models.CharField(max_length=40)
    Mobile = models.CharField(max_length=40)
    Email= models.CharField(max_length=40)
    Subject = models.CharField(max_length=40)
    Description = models.CharField(max_length=40)
    def __str__(self):
        return self.Name
