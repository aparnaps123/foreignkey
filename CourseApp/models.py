from django.db import models

# Create your models here.
class studentCourse(models.Model):
    course_name=models.CharField(max_length=255,null=True)
    fee=models.IntegerField(null=True)

class student(models.Model):
    course=models.ForeignKey(studentCourse,on_delete=models.CASCADE,null=True)
    student_name=models.CharField(max_length=255,null=True)
    student_address=models.CharField(max_length=255)
    student_age=models.IntegerField(null=True,blank=True,default=1)
    joining_date=models.DateField()
