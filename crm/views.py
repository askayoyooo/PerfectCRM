from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def stu_index(request):
    return render(request, 'student/student.html')


def customer_list(request):
    return render(request, 'sales/customer.html')