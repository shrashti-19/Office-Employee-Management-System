from django.contrib import admin
from .models import Employee,Role,PerformanceReview,Attendance,Task,Department
# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(PerformanceReview)
admin.site.register(Attendance)
admin.site.register(Task)
admin.site.register(Department)

