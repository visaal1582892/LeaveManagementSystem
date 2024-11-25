from django.db import models
from django.contrib.auth.models import User
class Colleges(models.Model):
    college_name=models.CharField(max_length=100)
class Department(models.Model):
    dept_name=models.CharField(max_length=50)
class Faculty(models.Model):
    employee_id=models.CharField(primary_key=True,max_length=20)
    faculty_name=models.CharField(max_length=100)
    dept_id=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,default=None)
    college_id=models.ForeignKey(Colleges,on_delete=models.CASCADE,null=True,default=None)
    user_id=models.ForeignKey(User,unique=True,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)
    aadhar=models.CharField(max_length=12)
    designation=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    employment_type=models.CharField(max_length=20)
    employment_status=models.CharField(max_length=20)
    leave_balance=models.JSONField()