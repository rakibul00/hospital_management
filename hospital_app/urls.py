
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('contact/', views.contact,name='contact'),
    path('doc_appiomnet/', views.doc_appioment,name='doc_app'),
    path('service/', views.service,name='service'),
    path('doctor/<int:id>/', views.doctor_detail, name='doctor_detail'),
    path('our_doc/', views.our_doctor,name='our_doc'),
    path('success/', views.appointment_success, name='appointment_success'),


]
