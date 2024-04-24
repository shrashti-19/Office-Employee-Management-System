from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from datetime import datetime
from django.db.models import Q 

def index(request):
    return render(request ,'index.html' )

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            address = request.POST.get('address')
            hire_date = datetime.strptime(request.POST.get('hire_date'), '%Y-%m-%d')
            department_id = request.POST.get('department')
            role_id = request.POST.get('role')
            salary = request.POST.get('salary')

            new_emp = Employee.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=address,
                hire_date=hire_date,
                department_id=department_id,
                role_id=role_id,
                salary=salary
            )
        
            return HttpResponse("Employee added successfully!")
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Invalid request method")

def remove_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request ,'remove_emp.html',context )


def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        department=request.POST['department']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if department:
            emps=emps.filter(department__name=department)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request ,'filter_emp.html' )
    else:
        return HttpResponse('an error occurred')
def performance_review(request):
     if request.method == 'POST':
        try:
            employee_id = request.POST.get('employee')
            employee = Employee.objects.get(pk=employee_id)
            review_date = request.POST.get('review_date')
            reviewer = request.POST.get('reviewer')
            rating = int(request.POST.get('rating'))
            comments = request.POST.get('comments')

            # Convert review_date string to datetime object
            review_date_obj = datetime.strptime(review_date, '%Y-%m-%d').date()

            # Create and save the PerformanceReview object
            performance_review.objects.create(
                employee=employee,
                review_date=review_date_obj,
                reviewer=reviewer,
                rating=rating,
                comments=comments
            )

            # Fetch employee list again
            employees = Employee.objects.all()
            return render(request, 'performance_review.html', {'employees': employees, 'success_message': 'Performance review submitted successfully!'})

        except Exception as e:
            return render(request, 'performance_review.html', {'error_message': str(e)})

     elif request.method == 'GET':
        # Fetch employee list for the dropdown
        employees = Employee.objects.all()
        return render(request, 'performance_review.html', {'employees': employees})

     else:
        return HttpResponse('Invalid request method', status=405)
def attendance(request):
    from django.shortcuts import render
from .models import Employee, Attendance
from datetime import datetime

def attendance(request):
    if request.method == 'POST':
        try:
            employee_id = request.POST.get('employee')
            employee = Employee.objects.get(pk=employee_id)
            date = request.POST.get('date')
            time_in = request.POST.get('time_in')
            time_out = request.POST.get('time_out')

            # Convert date and time strings to datetime objects
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            time_in_obj = datetime.strptime(time_in, '%H:%M').time()
            time_out_obj = datetime.strptime(time_out, '%H:%M').time()

            # Create and save the Attendance object
            Attendance.objects.create(
                employee=employee,
                date=date_obj,
                time_in=time_in_obj,
                time_out=time_out_obj
            )

            # Fetch employee list again
            emps = Employee.objects.all()
            return render(request, 'attendance.html', {'emps': emps, 'success_message': 'Attendance recorded successfully!'})

        except Exception as e:
            return render(request, 'attendance.html', {'error_message': str(e)})

    elif request.method == 'GET':
        emps = Employee.objects.all()
        return render(request, 'attendance.html', {'emps': emps})

    else:
        return render(request, 'attendance.html', {'error_message': 'Invalid request method'})

