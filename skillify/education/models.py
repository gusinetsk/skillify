from django.db import models


SEX = [
    ('m', 'male'),
    ('f', 'female')
    ]

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(max_length=1,choices=SEX)
    email = models.EmailField(null=True)
    group = models.IntegerField()
