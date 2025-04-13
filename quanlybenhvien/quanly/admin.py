from django.contrib import admin

# Register your models here.
from .models import Post, Patient, Appointment, MedicalRecord, Service, Invoice,  Prescription, InvoiceService,Doctor,Medicine

admin.site.register(Post)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Service)
admin.site.register(Invoice)
admin.site.register(Prescription)
admin.site.register(InvoiceService)
admin.site.register(Doctor)
admin.site.register(Medicine)

