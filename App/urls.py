from App import views
from django.urls import path

app_name = "App"

urlpatterns = [
    path("", views.loginuser, name="login"),
    path("login/",views.loginuser, name="login"),
    path("register/", views.register, name="register"),
    path("index/", views.index, name="index"),
    path("create-resume/", views.create_resume, name="create-resume"),
    path("resume/", views.resume, name="resume"),
    path("srt-resume/", views.resumesrt, name="resume"),
    # path("upload_csv",views.upload_csv, name="upload_csv"),
    path("logout/",views.logoutuser, name="logout"),
    
]