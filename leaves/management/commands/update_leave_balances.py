from django.core.management.base import BaseCommand
import json
from registration.models import Faculty
from leaves.models import *
class Command(BaseCommand):
    def handle(self):
        faculty_rows=Faculty.objects.get(gender="male",employment_type="teaching",employment_status="regular")
        for row in faculty_rows:
            leave_balance=json.loads(row.leave_balance)
            leave_balance_fixed=leave_balance["fixed"]
            default=male_teaching_regular
            default["fixed"]=leave_balance_fixed
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="male",employment_type="teaching",employment_status="contract")
        for row in faculty_rows:
            default=male_teaching_contract
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="male",employment_type="non_teaching",employment_status="regular")
        for row in faculty_rows:
            leave_balance=json.loads(row.leave_balance)
            leave_balance_fixed=leave_balance["fixed"]
            default=male_non_teaching_regular
            default["fixed"]=leave_balance_fixed
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="male",employment_type="non_teaching",employment_status="contract")
        for row in faculty_rows:
            default=male_non_teaching_contract
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="female",employment_type="teaching",employment_status="regular")
        for row in faculty_rows:
            leave_balance=json.loads(row.leave_balance)
            leave_balance_fixed=leave_balance["fixed"]
            default=female_teaching_regular
            default["fixed"]=leave_balance_fixed
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="female",employment_type="teaching",employment_status="contract")
        for row in faculty_rows:
            default=female_teaching_contract
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="female",employment_type="non_teaching",employment_status="regular")
        for row in faculty_rows:
            leave_balance=json.loads(row.leave_balance)
            leave_balance_fixed=leave_balance["fixed"]
            default=female_non_teaching_regular
            default["fixed"]=leave_balance_fixed
            row.leave_balance=json.dumps(default)
            row.save()
        faculty_rows=Faculty.objects.get(gender="female",employment_type="non_teaching",employment_status="contract")
        for row in faculty_rows:
            default=female_non_teaching_contract
            row.leave_balance=json.dumps(default)
            row.save()