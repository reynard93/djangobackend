# from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Job(models.Model):
    job_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.job_name

    class Meta:
        unique_together = ('job_name', 'company')


class Employee(models.Model):
    jobs = models.ManyToManyField(Job, related_name='employees')
    name = models.CharField(max_length=200, unique=True)

    def total_time_worked(self):
        sum_h = 0
        sum_m = 0
        for entry in list(TimeEntry.objects.filter(employee=self, clock_out__isnull=False)):
            clock_in = entry.clock_in.split(':')
            clock_out = entry.clock_out.split(':')

            # convert time from string to integer
            clock_out_int_h = int(clock_out[0])
            clock_out_int_m = int(clock_out[1])
            clock_in_int_h = int(clock_in[0])
            clock_in_int_m = int(clock_in[1])

            # calculate Working Hours
            if clock_out_int_m > clock_in_int_m:
                hours = (clock_out_int_h - clock_in_int_h)
                minutes = (clock_out_int_m - clock_in_int_m)
            else:
                hours = (clock_out_int_h - clock_in_int_h) - 1
                minutes = 60 - (clock_in_int_m - clock_out_int_m)
            sum_h += hours
            sum_m += minutes
            # Collect Total Hours of the Employee
            if sum_m > 60:
                sum1 = (sum_m / 60)
                split_min = str(sum1).split('.')
                int_part = int(split_min[0])
                decimal = int((sum1 - int_part) * 60)
                total_hours = sum_h + int_part
                return total_hours, "Hours and", decimal, "Minutes"
            else:
                return sum_h, "Hours and", sum_m, "Minutes"


class TimeEntry(models.Model):
    clock_in = models.CharField(blank=True, null=True, max_length=5)
    clock_out = models.CharField(blank=True, null=True, max_length=5)
    date = models.DateTimeField(default=timezone.now)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='time_entries', null=True)

    def __str__(self):
        return 'id: %i, clock_in: %s, clock_out: %s' % (self.id, self.clock_in, self.clock_out)