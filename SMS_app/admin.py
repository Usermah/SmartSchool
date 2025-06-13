from django.contrib import admin
from .models import Teacher, Student, Classroom, Timetable

# Register your models here.
# admin.py

class StudentInline(admin.TabularInline):
    model = Student
    extra = 0

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'class_teacher']
    inlines = [StudentInline]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email']

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['classroom', 'subject', 'day', 'time']
    list_filter = ['day', 'classroom']
