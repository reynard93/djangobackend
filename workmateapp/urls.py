from django.urls import path, include
from rest_framework import routers
from workmateapp.viewsets import EmployeeViewset, TimeEntryViewset, JobViewset

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('time_entry', TimeEntryViewset)
router.register('job', JobViewset)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls))
]