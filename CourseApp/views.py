from django.shortcuts import render,redirect
from CourseApp.models import studentCourse,student

# Create your views here.
def fun(request):
    return render(request,'home.html')
def addcourse(request):
    return render(request,'addcourse.html')
def addcoursedb(request):
    if request.method == "POST":
        course_name=request.POST['Course']
        course_fee=request.POST['fee']
        course=studentCourse(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('/')
def student_reg(request):
    courses=studentCourse.objects.all()
    return render(request,'addstudent.html',{'course':courses})


def add_studentdb(request):
    if request.method =='POST':
        student_name=request.POST['student_name']
        student_address=request.POST['student_address']
        age=request.POST['student_age']
        jdate=request.POST['joining_date']
        sel=request.POST['course']
        coursel=studentCourse.objects.get(id=sel)
        Student=student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=coursel)
        Student.save()
        return redirect('/')
    
def showstudent(request):
    Student=student.objects.all()
    return render(request,'showstudent.html',{'students':Student})

def edit(request,pk):
    Student=student.objects.get(id=pk)

    course=studentCourse.objects.all()
    return render(request,'edit.html',{'stud':Student,'course':course})

def editdb(request,pk):
    if request.method=='POST':
        Student=student.objects.get(id=pk)
        Student.student_name=request.POST['student_name']
        Student.student_address=request.POST['student_address']
        Student.student_age=request.POST['student_age']
        Student.joining_date=request.POST['joining_date']
        sel=request.POST['course']
        coursel=studentCourse.objects.get(id=sel)
        Student.course=coursel
        Student.save()
        return redirect('showstudent')
    return render(request,'edit.html')

def delete(request,pk):
    s = student.objects.get(id=pk)
    s.delete()
    return redirect('showstudent')

