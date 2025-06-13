from django.db import models

# Create your models here.
# models.py

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    classroom = models.ForeignKey('Classroom', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=20)  # e.g., "JSS1A"
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day = models.CharField(max_length=10)  # e.g., "Monday"
    time = models.TimeField()

    def __str__(self):
        return f"{self.subject} - {self.classroom} - {self.day} - {self.time}"
    