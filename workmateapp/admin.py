from django.contrib import admin
from .models import Job, Employee, TimeEntry


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['job_name', 'company']
    list_filter = ['job_name', 'company']
    search_fields = ['job_name', 'company']


admin.site.register(Employee)

admin.site.register(TimeEntry)