# Generated by Django 5.0 on 2024-01-06 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaves', '0004_alter_leaves_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaves',
            name='applied_date',
            field=models.DateField(null=True),
        ),
    ]
