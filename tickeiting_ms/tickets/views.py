from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Ticket, SoftwareTicket, HardwareTicket, Employee, ITSpecialist, Center
from .serializers import TicketSerializer, SoftwareTicketSerializer, HardwareTicketSerializer
import uuid

@api_view(['POST'])
def create_ticket(request):
    try:
        employee = Employee.objects.get(name=request.data['employee_name'])
        center = employee.center
        it_specialist = ITSpecialist.objects.get(center_id=center.id)
        
        ticket_number = str(uuid.uuid4())
        ticket_data = {
            'ticket_number': ticket_number,
            'employee': employee.pk,
            'problem_description': request.data['problem_description'],
            'problem_type': request.data['problem_type'],
            'device_type': request.data['device_type'],
            'center': center.pk,
            'it_specialist': it_specialist.pk
        }
        
        # Save the base ticket
        ticket_serializer = TicketSerializer(data=ticket_data)
        if ticket_serializer.is_valid():
            ticket = ticket_serializer.save()
            
            # Additional details based on the problem type
            if request.data['problem_type'] == 'software':
                software_data = {
                    'ticket': ticket.id,
                    'os_version': request.data.get('os_version'),
                    'affected_app': request.data.get('affected_app'),
                    'error_code': request.data.get('error_code'),
                    'screenshot': request.FILES.get('screenshot')
                }
                software_serializer = SoftwareTicketSerializer(data=software_data)
                if software_serializer.is_valid():
                    software_serializer.save()
            
            elif request.data['problem_type'] == 'hardware':
                hardware_data = {
                    'ticket': ticket.id,
                    'device_serial_number': request.data.get('device_serial_number'),
                    'picture': request.FILES.get('picture')
                }
                hardware_serializer = HardwareTicketSerializer(data=hardware_data)
                if hardware_serializer.is_valid():
                    hardware_serializer.save()
            
            return Response({'ticket_number': ticket_number}, status=status.HTTP_201_CREATED)
        
        return Response(ticket_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
