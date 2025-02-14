
from django.shortcuts import render, get_object_or_404,redirect

from .forms import DoctorSearchForm,AppointmentForm
from .models import Doctor,DoctorCategory,Appointment
# Create your views here.
def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')




def doc_appioment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()
    return render(request, 'doc_appinment.html', {'form': form})

def appointment_success(request):
    form = Appointment.objects.all()
    return render(request, 'appointment_success.html',{'form':form})


def service(request):
     doc = Doctor.objects.all()
   
     return render(request, 'service.html',{'doc':doc})
  

def doctor_detail(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doc_detalis.html', {'doctor': doctor})






def our_doctor(request):
    form = DoctorSearchForm(request.GET or None)
    doctors = Doctor.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        specialization = form.cleaned_data.get('specialization')

        if name:
            doctors = doctors.filter(first_name__icontains=name) | doctors.filter(last_name__icontains=name)
        if specialization:
            doctors = doctors.filter(specialization=specialization)

    return render(request, 'our_doc.html', {'form': form, 'doctors': doctors})
