from rest_framework import serializers
from .models import Employee, TimeEntry, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_name', 'company', 'employees')


class TimeEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ('id', 'clock_in', 'clock_out', 'date')


class JobNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'job_name')


class EmployeeSerializer(serializers.ModelSerializer):
    jobs = serializers.StringRelatedField(many=True)
    time_entries = serializers.StringRelatedField(many=True)

    # i need to serialize jobs and time entries
    class Meta:
        model = Employee
        fields = ('id', 'name', 'jobs', 'time_entries', 'total_time_worked')



