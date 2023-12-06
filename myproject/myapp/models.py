# myapp/models.py

from django.db import models
from rest_framework.response import Response
from rest_framework import status



class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name', help_text='Enter student\'s first name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name', help_text='Enter student\'s last name')

class Rating(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='ratings', default=None, null=True, verbose_name='Student')
    value = models.FloatField(verbose_name='Rating Value')


