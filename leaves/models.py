from django.db import models
from registration.models import *

class Leaves(models.Model):
    year=models.IntegerField(null=True,blank=False)
    applied_date=models.DateTimeField(auto_now=True,null=True,blank=False)
    employee_id=models.ForeignKey(Faculty,on_delete=models.CASCADE,null=True,default=None)
    dept_id=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,default=None)
    start_date = models.DateField(null=True,blank=False)
    end_date = models.DateField(null=True,blank=False)
    number_of_days=models.SmallIntegerField()
    leave_type = models.CharField(max_length=25,null=True,blank=False)
    reason = models.CharField(max_length=255,null=True,blank=True)
    status = models.JSONField()

#different types of faculty and their default leave balances
male_teaching_regular={
    "variable" : {"Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,},
    "fixed" : {"Paternity Leaves" : 30,
    }
}
male_teaching_contract={
    "Casual Leaves" : 15
}
male_non_teaching_regular={
    "variable" : {"Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,},
    "fixed" : {
        "Paternity Leaves" : 30,
    }
}
male_non_teaching_contract={
    "Casual Leaves" : 15,
}
female_teaching_regular={
    "variable" : {"Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Academic Leaves" : 10,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,},
    "fixed" : {"Maternity Leaves" : 180,}
}
female_teaching_contract={
    "Casual Leaves" : 15
}
female_non_teaching_regular={
    "variable" : {"Casual Leaves" : 8,
    "Special Casual Leaves" : 7,
    "Optional Holidays" : 5,
    "Medical Leaves" : 5,},
    "fixed" : {"Maternity Leaves" : 180,}
}
female_non_teaching_contract={
    "Casual Leaves" : 15,
}

#different values of leave status
status_values=['pending','accepted','rejected']

#default value of status_json
status_default={
    "hod" : status_values[0],
    "principal" : status_values[0]
}
status_hod_accepted={
    "hod" : status_values[1],
    "principal" : status_values[0]
}
status_accepted={
    "hod" : status_values[1],
    "principal" : status_values[1]
}
status_rejected={
    "hod" : status_values[2],
    "principal" : status_values[2]
}
principal_status_default={
    "registrar" : status_values[0]
}
principal_status_registrar_accepted={
    "registrar" : status_values[1]
}
principal_status_registrar_rejected={
    "registrar" : status_values[2]
}
registrar_status_default={
    "vice chancellor" : status_values[0]
}
registrar_status_viceChancellor_accepted={
    "vice chancellor" : status_values[1]
}
registrar_status_viceChancellor_rejected={
    "vice chancellor" : status_values[2]
}
