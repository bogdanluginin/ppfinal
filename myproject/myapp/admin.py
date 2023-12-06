# myapp/admin.py

from django.contrib import admin
from .models import Student, Rating

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    list_filter = ('last_name',)  # Enable filtering by last name
    search_fields = ('first_name', 'last_name')  # Enable search by first name or last name
    ordering = ('last_name', 'first_name')  # Default ordering

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'student')
    list_filter = ('value',)  # Enable filtering by value
    search_fields = ('student__first_name', 'student__last_name')  # Enable search by student's first name or last name
    ordering = ('-value',)  # Default ordering
