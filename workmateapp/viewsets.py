from datetime import datetime

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from . import serializers
from .models import Employee, TimeEntry, Job
from .serializers import TimeEntrySerializer


class JobViewset(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


class TimeEntryViewset(viewsets.ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = serializers.TimeEntrySerializer

    @action(detail=False, methods=['POST'])
    def clock_in(self, request):
        if 'name' in request.data:
            # should probably check against employee id with login sys
            try:
                employee = Employee.objects.get(name=request.data['name'])
                currently_clocked_in = TimeEntry.objects.filter(employee=employee, clock_out__isnull=True).order_by('-date')
                if len(currently_clocked_in):
                    serializer = TimeEntrySerializer(currently_clocked_in[0], many=False)
                    return Response({
                        'message': 'cannot check in again, use put to check out',
                        'result': serializer.data
                    }, status=status.HTTP_400_BAD_REQUEST)
                time_entry = TimeEntry.objects.create(
                    employee=employee,
                    date=timezone.now(),
                    clock_in=datetime.now().strftime('%H:%M')
                )
                # print(time_entry, 'have time entry')
                serializer = TimeEntrySerializer(time_entry, many=False)

                return Response({
                    'message': 'clocked in',
                    'result': serializer.data
                }, status=status.HTTP_200_OK)
            except:
                # create new time entry try confirm is because of no currently_clocked_in by finding employee again
                employee = Employee.objects.get(name=request.data['name'])
                time_entry = TimeEntry.objects.create(
                    employee=employee,
                    date=timezone.now(),
                    clock_in=datetime.now().strftime('%H:%M')
                )
                serializer = TimeEntrySerializer(time_entry, many=False)

                return Response({
                    'message': 'clocked in',
                    'result': serializer.data
                }, status=status.HTTP_200_OK)
        else:
            return Response('you need to be a worker to check in', status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PUT'])
    def clock_out(self, request, pk=None):
        # // with validation
        try:
            time_entry = TimeEntry.objects.get(id=pk)
            if time_entry.clock_out is None:
                time_entry.clock_out = datetime.now().strftime('%H:%M')
                time_entry.save()
                serializer = TimeEntrySerializer(time_entry, many=False)
                return Response({
                    'message': 'clocked out',
                    'result': serializer.data
                }, status=status.HTTP_200_OK)
            else:
                return Response('already clocked out, invalid', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('time card with id,', pk, ' not found')
