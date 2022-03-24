from django.db import models
from django.forms import BooleanField
from django.contrib.auth.models import User
from django.utils import timezone
from numpy import empty


# class Company(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name

#     def list_company(self):
#         companies = [company for company in Company]
#         return companies


# class Language(models.Model):
#     name = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

# class Programmers(models.Model):
#     name = models.CharField(max_length=20)
#     company = models.ForeignKey(Company,on_delete=models.CASCADE)
#     is_true = models.BooleanField(default=True)
#     languages = models.ManyToManyField(Language)

    

#     def __str__(self):
#         return self.name

#     def list_programmers(self):
#         programmer = [programmer for programmer in Programmers]
#         return programmer


class Post(models.Model):
     name = models.CharField(max_length=20)
     username = models.ForeignKey(User,on_delete=models.CASCADE)
     def __str__(self):
         return self.name

# class Car(models.Model):
#     name = models.CharField(max_length=20)
#     key = models.ManyToManyField(Post)
#     def __str__(self):
#         return self.name


# class Phone(models.Model):
#     name = models.CharField(max_length=20)
#     key = models.ManyToManyField(Post)
#     def __str__(self):
#         return self.name


class Todo(models.Model):
     date = models.DateTimeField()
     text = models.CharField(max_length=100)
     def __str__(self):
         return self.text

class Job(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    customer = models.CharField(max_length=200, default='Admin')
    description = models.CharField(max_length=300, null= True)

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        naira =4.19
        dollar = self.price/415.89
        return "{0:.2f}".format(dollar)