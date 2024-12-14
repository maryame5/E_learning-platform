import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import  Group
from django.views.decorators.csrf import csrf_protect

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "e_learning/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "e_learning/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "e_learning/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        type = request.POST["user_type"]
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            if type == "student":
                Student.objects.create(student_user=user).save()
                student_group, created = Group.objects.get_or_create(name='Teachers')
                user.groups.add(student_group)
            elif type == "teacher":
                Teacher.objects.create(teacher_user=user).save()
                teacher_group, created = Group.objects.get_or_create(name='Teachers')
                user.groups.add(teacher_group)
            elif type == "admin":
                Admin.objects.create(admin_user=user).save()
                teacher_group, created = Group.objects.get_or_create(name='Teachers')
                student_group, created = Group.objects.get_or_create(name='Teachers')
                user.groups.add(teacher_group)
                user.groups.add(student_group)
            
        except IntegrityError:
            return render(request, "e_learning/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "e_learning/register.html")

def index(request):
    user= request.user
    if user.is_authenticated:
        user1= User.objects.get(username=user.username)
        try:
            teacher= Teacher.objects.get(teacher_user=user1)
            subjects= Subject.objects.all()
            return render(request, "e_learning/index.html",{
                "teacher": teacher,
                "subjects": subjects,
                "message": "You are  a teacher."
            })
        except Teacher.DoesNotExist:
            try:
                students= Student.objects.get(student_user=user1)
                subjects= Subject.objects.all()
                return render(request, "e_learning/index.html",{
                        "student": students,
                        "subjects": subjects,
                        "message": "You are  a student."})
            except Student.DoesNotExist:
                try:
                    admin= Admin.objects.get(admin_user=user1)
                    subjects= Subject.objects.all()

                    return render(request, "e_learning/index.html",{
                        "admin": admin,
                        "subjects": subjects,
                        "message": "You are  a admin."

                    })
                except Admin.DoesNotExist:
                    return render(request, "e_learning/index.html", {
                        "subjects": Subject.objects.all(),

                  "message": "You are a guest."})
    else:
         return render(request, "e_learning/index.html", {
                        "message": "Please log in to access this page."
          })
def profil(request):
    return render(request,"e_learning/index.html")

@csrf_exempt
@login_required
def create_subject(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            creator = data.get("teacher")
            user= User.objects.get(username=creator)
            teacher = Teacher.objects.get(teacher_user=user)
            name= data.get("name")
            description= data.get("description")
            print(f"Received data: {data}")

            if not name :
                return JsonResponse({"Name is required"}, status=400)
            if not description :
                return JsonResponse("Description is required", status=400)
            subject = Subject.objects.create(subject_name=name , subject_description=description,teacher=teacher)
            subject.save()
            return HttpResponseRedirect(reverse("index"))

        
        except json.JSONDecodeError:
            return JsonResponse("Invalid JSON", status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=400)
    
         
    return render(request, "e_learning/create_subject.html")

@login_required
def subject(request,name):
    user=request.user
    user1=User.objects.get(username=user)
    teachers=Teacher.objects.all()
    try:
        student=Student.objects.get(student_user=user1)
        student_user=student.student_user
        student_name=student_user.username
    except Student.DoesNotExist:
        student=0
        student_name=0
    subject = Subject.objects.get(subject_name=name)
    courses = subject.course.all() 
    print(user,student_name)
    opened_courses = opened_course.objects.filter(student__student_user=user).values_list('course', flat=True)
    for course in courses:
         course.is_open = course.id in opened_courses 
                    


    return render(request, "e_learning/subject.html",{
        "subject": subject,
        "teachers":teachers,
        "student_name":student_name,
        "courses": courses,
        "userr": user.username,
        
    })

@login_required
def enrolling(request,subject)   :
    if request.method == "POST":
            #user connected
            user=request.user
            user1=User.objects.get(username=user)
            student = Student.objects.get(student_user=user1)
            subjects = Subject.objects.get(subject_name=subject)
            
            #create relation between the user and the posts he wanna start following
            try :
                enroll.objects.get(student=student, subject=subjects)
            
            except enroll.DoesNotExist:

                enroll.objects.create(student=student, subject=subjects)
            return HttpResponseRedirect(reverse('subject', args=[subject]))
    return JsonResponse({"error": "Invalid request method."}, status=405)
@login_required
def unenrolling(request,subject)   :
    if request.method == "POST":
            #user connected
            user=request.user
            user1=User.objects.get(username=user)
            student = Student.objects.get(student_user=user1)
            subjects = Subject.objects.get(subject_name=subject)
                #create relation between the user and the posts he wanna start following
            try :
                enroll.objects.get(student=student, subject=subjects).delete()
            except enroll.DoesNotExist:
                message = "you should be enrolling this subject first "

                
            return HttpResponseRedirect(reverse('subject', args=[subject],))
    return JsonResponse({"error": "Invalid request method."}, status=405)
@csrf_exempt
@login_required
def create_course(request):
    if request.method == "POST":
        try:
            image=request.FILES.get("course_image")
            document= request.FILES.get("course_documents")
        
            creator = request.user
            user= User.objects.get(username=creator)
            teacher = Teacher.objects.get(teacher_user=user)
            name= request.POST.get("name")
            subject_name= request.POST.get("subject_name")
            content= request.POST.get("content")
           
           
            subjects= Subject.objects.filter(teacher=teacher)
            print("subjects",subjects)
            print(f"Received data: {image,document}")

            if not name or not content:
                return HttpResponse({"Name is required"}, status=400)
            
            course= Course.objects.create(course_name=name,course_content=content,course_documents=document,course_image=image)
            course.save()
            subject = Subject.objects.get(subject_name=subject_name )
            subject.course.add(course)
            return HttpResponseRedirect(reverse("index"))

        except Exception as e:
            return HttpResponse({"error": f"Error: {str(e)}"}, status=400)
    if request.method == "GET":
        user = request.user
        try:
            teacher = Teacher.objects.get(teacher_user=user)
            subjects = Subject.objects.filter(teacher=teacher)
        except Teacher.DoesNotExist:
            subjects = []
    
         
    return render(request, "e_learning/create_course.html",{
        "subjects":subjects
    })
@csrf_exempt
@login_required
def course(request,name):
    
    course = Course.objects.get(course_name=name)
    subject = Subject.objects.get(course=course)
    if request.method=="GET":
         return render(request, "e_learning/course.html",{"course":course,
                                                     "subject":subject})
    elif request.method=="PUT":
        data = json.loads(request.body)
        user=User.objects.get(username=request.user)
        if data.get("is_open") is not None:
            if data["is_open"] is True:
                try :
                     student = Student.objects.get(student_user=user)
                     try:
                         opened=opened_course.objects.get(student=student,course=course)
                         return JsonResponse({"message": "Course already opened"}, status=400)
                     except opened_course.DoesNotExist:
                            opened= opened_course.objects.create(student=student,course=course)
                            opened.save()
                            return JsonResponse({"message": "Course opened"}, status=200)
                except Student.DoesNotExist:
                    return HttpResponse({"message": "You are not a student"}, status=400)
                         
                         
        
@csrf_exempt 
@login_required
def delete_course(request):
    creator=request.user
    user= User.objects.get(username=creator)
    if request.method == "POST":
        try: 
             teacher = Teacher.objects.get(teacher_user=user)
             
             subjects= Subject.objects.filter(teacher=teacher)
             courses=[]
        
             for subject in subjects:
                  for course1 in subject.course.all():
                     courses.append(course1)
             data=json.loads(request.body)
             course_name = data.get("course_name")
             subject_name=data.get("subject_name")
             course = Course.objects.get(course_name=course_name)
             subject=Subject.objects.get(subject_name=subject_name)
             if course not in subject.course.all():
                error= "Course not found in the selected subject."
                return render(request,"e_learning/delete_course.html",
                      
                  {"courses":courses,
                   "error":error,
                   "subjects":subjects})

             if teacher==subject.teacher:
            
                subject.course.remove(course)
                subject.save()
                course.delete()
                return HttpResponseRedirect(reverse("index"))
         
             else:
               error= "You do not have permission to delete this course."
               return render(request,"e_learning/delete_course.html",
                      
                  {"courses":courses,
                   "error":error,
                   "subjects":subjects})

        except json.JSONDecodeError:
            return JsonResponse({"error":"Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Error: {str(e)}"}, status=400)
    else:
        teacher = Teacher.objects.get(teacher_user=user)
        subjects= Subject.objects.filter(teacher=teacher)
        courses=[]
        
        for subject in subjects:
             for course in subject.course.all():
                 courses.append(course)
             
    
        return render(request,"e_learning/delete_course.html",
                      
                  {"courses":courses,
                
                   "subjects":subjects})
        
@login_required          
def enrolled_subject(request):
    user=request.user
    user1=User.objects.get(username=user)
    try:
        student=Student.objects.get(student_user=user1)
    except Student.DoesNotExist:
        student=0

    enrolled=enroll.objects.filter(student=student)
    enrolled_su=[]
    for i in enrolled:
        enrolled_su.append(i.subject)
    return render(request,"e_learning/enrolled_subject.html",{
                  "student":student,
                  "enrolled_su" :enrolled_su
                  })
@login_required
def my_subject(request):
    user=request.user
    user1=User.objects.get(username=user)
    try :
        teacher=Teacher.objects.get(teacher_user=user1)
        subjects= Subject.objects.filter(teacher=teacher)
        return render (request,"e_learning/my_subject.html",{
            "subjects":subjects,
        })
    except Teacher.DoesNotExist:
       return HttpResponseRedirect('not_authorized')
    
def not_authorized(request):
    return render(request,"e_learning/not_authorized.html")

