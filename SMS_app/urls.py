from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_student, name='add_student'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('classrooms/', views.classroom_list, name='classroom_list'),
    path('timetable/<int:class_id>/', views.timetable_view, name='timetable'),
    path('classroom/<int:class_id>/students/', views.students_in_class, name='students_in_class'),

]