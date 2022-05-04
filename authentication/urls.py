from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import SignupView, CreateStudentView, face_authentication_view

urlpatterns = [
    path("login/", obtain_auth_token),
    path("register/", SignupView.as_view()),
    path("new_student/", CreateStudentView.as_view()),
    path("face_auth/", face_authentication_view),
]
