from django.db import models

# Create your models here.
from django.db import models

class DoctorCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    specialization = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE, related_name='doctors')
    years_of_experience = models.IntegerField()
    date_joined = models.DateField(auto_now_add=True)
    education = models.CharField(max_length=100, default="Unknown")
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    def __str__(self):
        return f" {self.first_name} -- {self.specialization}"
    
    
    
    
class Appointment(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    patient_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    doctor_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    doctor_dep = models.ForeignKey(DoctorCategory, on_delete=models.CASCADE)
    address = models.TextField()

    date = models.DateField()
    time = models.TimeField()
  

    def __str__(self):
        return f"Appointment with  {self.doctor_name} "
