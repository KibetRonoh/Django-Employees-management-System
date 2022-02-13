from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list': employee_list
    }
    return render(request, "employee_register/employee_list.html", context)


def employee_form(request):
    if request.method == ['GET']:
        form = EmployeeForm()
        return render(request, "employee_register/employee_form.html", {"form": form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/list')


def employee_delete(request):
    return