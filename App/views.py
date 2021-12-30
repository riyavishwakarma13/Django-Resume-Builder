from django.shortcuts import render, redirect
from django.contrib import messages
from .models import createResume
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user have entered login credentials
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            # A backend authenticated the credentials
            return redirect("/index/")
        else:
            # No backend authenticated the credentials
            return redirect("/login/")
    return render(request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect("/login/")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return redirect("/")
    return render(request, "register.html")


def index(request):
    return render(request, "index.html")

def resumesrt(request):
    return render(request, "srt-resume.html")


def create_resume(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        aboutyou = request.POST.get('aboutyou')
        careerobj = request.POST.get('careerobj')
        ssc=request.POST.get('ssc')
        hsc=request.POST.get('hsc')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        cgpa=request.POST.get('cgpa')
        comname3=request.POST.get('comname3')
        j3sd = request.POST.get('j3sd')
        j3ed = request.POST.get('j3ed')
        positiondet3 = request.POST.get('positiondet3')
        comname2=request.POST.get('comname2')
        j2sd = request.POST.get('j3sd')
        j2ed = request.POST.get('j3ed')
        positiondet2 = request.POST.get('positiondet2')
        comname1=request.POST.get('comname1')
        j1sd = request.POST.get('j1sd')
        j1ed = request.POST.get('j1ed')
        positiondet1 = request.POST.get('positiondet1')
        references = request.POST.get('references')
        user=request.user
        template="resume.html"
        print(11)
        create_resume = createResume(user=user,template=template,name=name,comname1=comname1,comname2=comname2,comname3=comname3, address=address, phone=phone, email=email, aboutyou=aboutyou, careerobj=careerobj, ssc=ssc, hsc=hsc, college=college, degree=degree, cgpa=cgpa, j3sd=j3sd,j3ed=j3ed, positiondet3=positiondet3, j2sd=j2sd, j2ed=j2ed, positiondet2=positiondet2, j1sd=j1sd, j1ed=j1ed, positiondet1=positiondet1, references=references)
        print(12)
        create_resume.save()
        messages.success(request, "Your Info has been saved")
    return render(request, "create-resume.html")

def resume(request):
    try:
        print("hello")
        resume_info = createResume.objects.filter(user = request.user).first()
        print(resume_info.__dict__)
        context = {"resume_info": resume_info}
        return render(request, "resume.html", context)
    except Exception as e:
        print(e)
        print("hello2")
        return render(request, "resume.html")

# def upload_csv(request):
#     if request.method=="POST":
#         print("Hello")
#     return render(request,"index.html")