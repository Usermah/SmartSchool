# forms.py
from django import forms
from .models import Student, Teacher, Classroom, Timetable

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'date_of_birth', 'classroom']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'subject']

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'class_teacher']

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['classroom', 'teacher', 'subject', 'day', 'time']
