from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Teacher, Classroom, Timetable
from .forms import StudentForm, TeacherForm, ClassroomForm, TimetableForm
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def about(request):
    return render(request, 'about.html')

def home(request):
    students = Student.objects.count()
    teachers = Teacher.objects.count()
    classes = Classroom.objects.count()
    return render(request, 'home.html', {
        'students': students,
        'teachers': teachers,
        'classes': classes,
    })

def student_list(request):
    query = request.GET.get('q', '')
    student_list = Student.objects.select_related('classroom').all()
    
    if query:
        student_list = student_list.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query)
        )
    
    paginator = Paginator(student_list, 10)
    page = request.GET.get('page')
    students = paginator.get_page(page)
    
    return render(request, 'student_list.html', {
        'students': students,
        'query': query
    })

def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'add_student.html', {'form': form})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'add_teacher.html', {'form': form})

def classroom_list(request):
    classrooms = Classroom.objects.select_related('class_teacher').all()
    return render(request, 'classroom_list.html', {'classrooms': classrooms})

def timetable_view(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    timetable = Timetable.objects.filter(classroom=classroom).order_by('day', 'time')
    return render(request, 'timetable.html', {'classroom': classroom, 'timetable': timetable})

def students_in_class(request, class_id):
    classroom = get_object_or_404(Classroom, id=class_id)
    students = Student.objects.filter(classroom=classroom)

    return render(request, 'students_in_class.html', {
        'classroom': classroom,
        'students': students
    })
