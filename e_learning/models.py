from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass
    
   

class Student(models.Model):
    student_user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Teacher(models.Model):
    teacher_user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student,related_name="is_student")


class Admin(models.Model):
    admin_user = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    staff = models.ManyToManyField(Teacher,related_name="is_staff")


class Course(models.Model):
    course_name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    course_content=models.TextField(blank=True)
    course_documents=models.FileField(upload_to='documents/',null=True,blank=True)
    course_image=models.ImageField(upload_to='img/',null=True,blank=True)


class Subject(models.Model):
    subject_name = models.CharField(max_length=100 ,unique=True)
    subject_description =models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subject_teacher")
    course= models.ManyToManyField(Course ,related_name="course_subject")

