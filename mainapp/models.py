from django.db import models


# Create your models here.
class School(models.Model):
    """
    This model is used to create table of School
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(models.Model):
    """
    This model is used to create table of student in database.
    """
    name = models.CharField(max_length=255)
    enrollment_number = models.CharField(unique=True, max_length=255)
    school = models.ForeignKey(School, related_name="students_school", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
