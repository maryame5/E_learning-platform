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
    is_open=models.BooleanField(default=False)
    def serialize(self):
        return {
            "id": self.id,
            "course_name": self.course_name,
            "course_content": self.course_content,
            "course_documents": self.course_documents,
            "course_image": self.course_image,
            "created_at": self.created_at.strftime("%b %d %Y, %I:%M %p"),
            "is_open": self.is_open,
           
        }
    
    

class Subject(models.Model):
    subject_name = models.CharField(max_length=100 ,unique=True)
    subject_description =models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subject_teacher")
    course= models.ManyToManyField(Course ,related_name="course_subject")
    enrolled_by = models.ManyToManyField(Student, through='enroll' , through_fields=('subject', 'student'),related_name='enrolled_sub')

class enroll(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stud")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subje")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'subject')

class opened_course(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_opened")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student")
    created_at = models.DateTimeField(auto_now_add=True)
    is_open=models.BooleanField(default=False)
   
    class Meta:
        unique_together = ('student', 'course')

class comments(models.Model):
    subject=models.ForeignKey(Subject , on_delete=models.CASCADE, related_name="course_comments")
    student=models.ForeignKey(Student , on_delete=models.CASCADE, related_name="student_comments")
    comment=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


