from django.contrib import admin
from .models import Car, Company, Language, Phone, Post, Programmers,Todo
# Register your models here.
admin.site.register(Company)
admin.site.register(Programmers)
admin.site.register(Language)
admin.site.register(Post)
admin.site.register(Car)
admin.site.register(Phone)
admin.site.register(Todo)