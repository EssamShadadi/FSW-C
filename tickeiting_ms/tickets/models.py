from django.db import models

class Center(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ITSpecialist(models.Model):
    name = models.CharField(max_length=100)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    PROBLEM_TYPE_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software')
    ]
    DEVICE_TYPE_CHOICES = [
        ('Laptop', 'Laptop'),
        ('Mobile', 'Mobile'),
        ('Printer', 'Printer'),
        ('Access Point', 'Access Point')
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_process', 'In Process'),
        ('completed', 'Completed')
    ]
    
    ticket_number = models.CharField(max_length=150, unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    problem_description = models.TextField()
    problem_type = models.CharField(max_length=50, choices=PROBLEM_TYPE_CHOICES)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    it_specialist = models.ForeignKey(ITSpecialist, on_delete=models.CASCADE)
    center = models.ForeignKey(Center, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ticket {self.ticket_number} - {self.problem_type}"


class SoftwareTicket(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    os_version = models.CharField(max_length=50, blank=True, null=True)
    affected_app = models.CharField(max_length=50, blank=True, null=True)
    error_code = models.CharField(max_length=50, blank=True, null=True)
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)

    def __str__(self):
        return f"Software Ticket {self.ticket.ticket_number}"


class HardwareTicket(models.Model):
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    device_serial_number = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='hardware_pictures/', blank=True, null=True)

    def __str__(self):
        return f"Hardware Ticket {self.ticket.ticket_number}"
