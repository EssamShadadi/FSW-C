from django.contrib import admin
from .models import Center, Employee, ITSpecialist, Ticket, SoftwareTicket, HardwareTicket

# Register Center model
@admin.register(Center)
class CenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# Register Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'center']


# Register IT Specialist model
@admin.register(ITSpecialist)
class ITSpecialistAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'center']
 




# Register Ticket model
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'employee', 'problem_type', 'device_type', 'status', 'created_at', 'it_specialist']
   
# Register SoftwareTicket and HardwareTicket separately for management
@admin.register(SoftwareTicket)
class SoftwareTicketAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'os_version', 'affected_app', 'error_code']


@admin.register(HardwareTicket)
class HardwareTicketAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'device_serial_number']
