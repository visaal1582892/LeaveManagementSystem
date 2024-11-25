# Generated by Django 5.0 on 2024-01-03 11:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_remove_faculty_college_id_remove_faculty_dept_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('employee_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('aadhar', models.CharField(max_length=12)),
                ('designation', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('employment_type', models.CharField(max_length=20)),
                ('employment_status', models.CharField(max_length=20)),
                ('leave_balance', models.JSONField()),
                ('college_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.colleges')),
                ('dept_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.department')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
                ('section_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.section')),
            ],
        ),
    ]
