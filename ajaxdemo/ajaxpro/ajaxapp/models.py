from django.db import models

# Create your models here.
class dreamreal(models.Model):
    website = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    phonenumber = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)

class book(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.IntegerField()
    no_pages = models.IntegerField()