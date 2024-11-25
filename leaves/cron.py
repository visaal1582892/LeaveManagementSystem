# your_app/cron.py
from django_cron import CronJobBase, Schedule
from datetime import datetime

class UpdateLeaveBalancesCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00']  # Run at midnight
    MONTH = 1  # January
    DAY_OF_MONTH = 1  # 1st day of the month

    schedule = Schedule(run_at_times=RUN_AT_TIMES, run_every_mins=1)
    code = 'leaves.cron.UpdateLeaveBalancesCronJob'  # A unique code for this cron job

    def do(self):
        today = datetime.today()
        if today.month == self.MONTH and today.day == self.DAY_OF_MONTH:
            from django.core.management import call_command
            call_command('update_leave_balances')
