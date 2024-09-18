from rest_framework import serializers
from .models import Ticket, SoftwareTicket, HardwareTicket, Employee, ITSpecialist, Center

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 'name']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'center']


class ITSpecialistSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITSpecialist
        fields = ['id', 'name', 'center']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'ticket_number', 'employee', 'problem_description', 'problem_type', 'device_type', 'status', 'created_at', 'it_specialist', 'center']


class SoftwareTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareTicket
        fields = ['id', 'ticket', 'os_version', 'affected_app', 'error_code', 'screenshot']


class HardwareTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardwareTicket
        fields = ['id', 'ticket', 'device_serial_number', 'picture']
