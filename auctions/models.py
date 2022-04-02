from django.contrib.auth.models import AbstractUser
from django.db import models
from spacy import blank


class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length= 50)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    intial_price = models.FloatField()
    price = models.FloatField()

    description = models.TextField()
    image = models.ImageField(upload_to = 'Product',max_length = 1000,blank = True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name 
class Bid(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    auction = models.ForeignKey(Product,on_delete=models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now=True)

class WatchList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    def its_owner(self,user):
        return self.user == user
    def __str__(self) -> str:
        return f"{self.user} 's watchlist"
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.SET_NULL,null = True)
    body = models.TextField()

    def __str__(self) -> str:
        return self.body[:50]

