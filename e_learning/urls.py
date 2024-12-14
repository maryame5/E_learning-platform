from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profil",views.profil, name="profil"),
    path("create_subject",views.create_subject,name="create_subject"),
    path("subject/<str:name>",views.subject,name="subject"),
    path("create_course",views.create_course,name="create_course"),

    #path("edit_course",views.edit_course,name="edit_course"),
    path("delete_course",views.delete_course,name="delete_course"),
    path("course/<str:name>",views.course,name="course"),
    path("enrolling/<str:subject>",views.enrolling,name="enrolling"),
    path("unenrolling/<str:subject>",views.unenrolling,name="unenrolling"),
    path("enrolled_subject",views.enrolled_subject,name="enrolled_subject"),
    path("my_subject/",views.my_subject,name="my_subject"),
    path("not_authorized/",views.not_authorized,name="not_authorozed"),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)