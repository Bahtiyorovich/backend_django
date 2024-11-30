from django.shortcuts import render
# from itertools import count
from .models import Countries, Employees, Dependents
# from django.db.models import Q
# # Create your views here.
# from django.http import HttpResponse

def index_page(request):
    return render(request, "index.html")

def get_max_salary_employess(request, top):
    queryset = Employees.objects.all().order_by('-salary')[:top]
    return render(request, 'max_salary.html', {"max_salary": queryset})

def get_dependents(request, employee_id):
    queryset = Dependents.objects.all().filter(employee=employee_id)
    employee = Employees.objects.get(employee_id=employee_id)
    context = {'employee': employee, 'deps': queryset}
    return render(request, 'dependents.html', context)

def register(request):
    return render(request, 'register.html')

# def orm_list(request):
    # queryset = Countries.objects.all()
    # queryset = Countries.objects.only("country_name")
    # queryset = Countries.objects.filter(region_id=2)
    # queryset = Countries.objects.filter(country_name__startswith="I")
    # queryset = Countries.objects.filter(Q(country_name__startswith="A")|
    #                                     Q(country_name__endswith="B"))
    # queryset = Countries.objects.filter(Q(country_name__startswith="B")&
    #                                       Q(country_name__endswith="A"))
    # res = ""
    # for query in queryset:
    #     res += f"<li>{query.country_name}</li>"
    # return HttpResponse(f"<ul>{res}</ul>")

# def orm_list(request):
#     employees = Employees.objects.filter(Q(first_name__startswith="A")|
#                                          Q(last_name__startswith="B"))
#     # employees = Employees.objects.values('first_name', 'last_name')
#     print(employees.query)
#     employe = ""
#     for emp in employees:
#         # employe += f"{emp['first_name']} {emp['last_name']} <br>"
#         employe += f"{emp.first_name} {emp.last_name} <br>"
#     return HttpResponse(employe)








