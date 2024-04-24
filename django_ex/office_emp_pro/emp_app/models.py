from django.db import models
from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    hire_date = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Role(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Attendance(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date = models.DateField()
    time_in = models.TimeField()
    time_out = models.TimeField()

    def __str__(self):
        return f"{self.employee} - {self.date}"

class PerformanceReview(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    review_date = models.DateField()
    reviewer = models.CharField(max_length=100)
    rating = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Review for {self.employee} - {self.review_date}"
from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO')
    def __str__(self):
        return self.title
