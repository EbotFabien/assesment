# Generated by Django 5.0.4 on 2024-05-03 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk_assessment_project', '0008_rename_status_riskassessment_statu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riskassessment',
            name='statu',
        ),
    ]