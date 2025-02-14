# filepath: /Users/user/Desktop/django/hospital_management/hospital_app/forms.py
from django import forms
from .models import Doctor,DoctorCategory,Appointment

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'specialization', 'years_of_experience', 'image']
        
        


class DoctorSearchForm(forms.Form):
    name = forms.CharField(label="Doctor's Name", max_length=100, required=False)
    specialization = forms.ModelChoiceField(
        queryset=DoctorCategory.objects.all(),
        required=False,
        empty_label="Select Specialization"
    )
    
    
    
    
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name','email','phone_number','age','gender','doctor_name','doctor_dep','address', 'date', 'time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
 