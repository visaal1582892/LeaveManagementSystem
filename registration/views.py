from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from LeaveManagementSystem.settings import *
from registration.models import *
from leaves.models import *
import json
def home(request):
    return render(request,'registration/home.html')
def register(request):
    if request.method=="POST":
        college_name=request.POST['college_name']
        employee_id=request.POST['employee_id']
        if Faculty.objects.filter(employee_id=employee_id):
            messages.error(request,"Given Employee Id already already exists")
            return redirect('home')
        username=request.POST['username']
        if User.objects.filter(username=username):
            messages.error(request,"Given Username already exists")
            return redirect('home')
        gender=request.POST['gender']
        phone=request.POST['phone']
        if Faculty.objects.filter(phone=phone):
            messages.error(request,"Given phone number already already exists")
            return redirect('home')
        aadhar=request.POST['aadhar']
        if Faculty.objects.filter(aadhar=aadhar):
            messages.error(request,"Given aadhar number already exists")
            return redirect('home')
        email=request.POST['email']
        if User.objects.filter(email=email):
            messages.error(request,"Given Gmail Id already exists")
            return redirect('home')
        department_name=request.POST['department_name']
        designation=request.POST['designation']
        employment_type=request.POST['employment_type']
        employment_status=request.POST['employment_status']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password!=confirm_password:
            messages.error(request,"Passwords do not match")
            return redirect('register')
        current_college=Colleges.objects.get(college_name=college_name)
        current_dept=Department.objects.get(dept_name=department_name)
        if gender=="male" and employment_type=="teaching" and employment_status=="regular":
            leave_balance=json.dumps(male_teaching_regular)
        elif gender=="male" and employment_type=="teaching" and employment_status=="contract":
            leave_balance=json.dumps(male_teaching_contract)
        elif gender=="male" and employment_type=="non_teaching" and employment_status=="regular":
            leave_balance=json.dumps(male_non_teaching_regular)
        elif gender=="male" and employment_type=="non_teaching" and employment_status=="contract":
            leave_balance=json.dumps(male_non_teaching_contract)
        elif gender=="female" and employment_type=="teaching" and employment_status=="regular":
            leave_balance=json.dumps(female_teaching_regular)
        elif gender=="female" and employment_type=="teaching" and employment_status=="contract":
            leave_balance=json.dumps(female_teaching_contract)
        elif gender=="female" and employment_type=="non_teaching" and employment_status=="regular":
            leave_balance=json.dumps(female_non_teaching_regular)
        elif gender=="female" and employment_type=="non_teaching" and employment_status=="contract":
            leave_balance=json.dumps(female_non_teaching_contract)
        current_user=User.objects.create_user(username,email,password)
        current_user.save()
        current_faculty=Faculty(employee_id=employee_id,faculty_name=username,phone=phone,aadhar=aadhar,designation=designation,gender=gender,employment_type=employment_type,employment_status=employment_status,leave_balance=leave_balance,college_id=current_college,dept_id=current_dept,user_id=current_user)
        current_faculty.save()
        messages.success(request,"You are successfully registered")
        subject="Welcome Email"
        message="Hi {{ current_user.username }} !\nWe are glad to have you with Jntu Gv Leave Management System"
        from_email=EMAIL_HOST_USER
        receiversList=[current_user.email]
        send_mail(subject=subject,message=message,from_email=from_email,recipient_list=receiversList,fail_silently=True)
        return redirect('login')
    return render(request,'registration/register.html')
def login(request):
    if request.method=="POST":
        employee_id=request.POST['employee_id']
        password=request.POST['password']
        user=authenticate(username=employee_id,password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request,"You are successfully logged in")
            current_faculty=Faculty.objects.get(user_id=user.pk)
            if current_faculty.designation=='Employee':
                pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(status_default))
            elif current_faculty.designation=='HOD':
                pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(status_hod_accepted))
            elif current_faculty.designation=='Principal':
                pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(principal_status_default))
            elif current_faculty.designation=='Registrar':
                pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(registrar_status_default))
            elif current_faculty.designation=='Vice Chancellor':
                pending_leaves=None
            params={"faculty" : current_faculty,"leave_balance" : json.loads(current_faculty.leave_balance),"pending_leaves" : pending_leaves}
            return render(request,'registration/index.html',params)
        else:
            messages.error(request,"Not Yet Registered")
            return redirect('home')
    return render(request,'registration/login.html')
def index(request):
    current_faculty=Faculty.objects.get(user_id=request.user.pk)
    if current_faculty.designation=='Employee':
        pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(status_default))
    elif current_faculty.designation=='HOD':
        pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(status_hod_accepted))
    elif current_faculty.designation=='Principal':
        pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(principal_status_default))
    elif current_faculty.designation=='Registrar':
        pending_leaves=Leaves.objects.filter(employee_id=current_faculty,status=json.dumps(registrar_status_default))
    elif current_faculty.designation=='Vice Chancellor':
        pending_leaves=None
    params={"faculty" : current_faculty,"leave_balance" : json.loads(current_faculty.leave_balance),"pending_leaves" : pending_leaves}

    return render(request,'registration/index.html',params)
def logout(request):
    auth_logout(request)
    messages.success(request,"You are successfully logged out")
    return redirect('home')