# Generated by Django 5.1.6 on 2025-02-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_app', '0006_alter_appointment_patient_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(max_length=100),
        ),
    ]
