from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Tiêu đề bài viết
    content = models.TextField()  # Nội dung bài viết
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo

    def __str__(self):
        return self.title
        from django.db import models



# 1. Bảng bệnh nhân
class Patient(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.full_name

# 2. Bảng bác sĩ
class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.full_name

# 3. Bảng lịch hẹn
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"{self.patient.full_name} with {self.doctor.full_name} on {self.appointment_date}"

# 4. Bảng hồ sơ bệnh án
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    record_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Record {self.id} for {self.patient.full_name}"

# 5. Bảng dịch vụ
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.service_name

# 6. Bảng hóa đơn
class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} - {self.patient.full_name}"

# 7. Bảng thuốc
class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.medicine_name

# 8. Bảng đơn thuốc
class Prescription(models.Model):
    record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=50, blank=True)
    quantity = models.IntegerField()
    usage_instruction = models.TextField(blank=True)

    def __str__(self):
        return f"{self.medicine.medicine_name} for Record {self.record.id}"

# Bảng trung gian giữa hóa đơn và dịch vụ
class InvoiceService(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.service.service_name} x{self.quantity} in Invoice {self.invoice.id}"
