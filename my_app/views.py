from itertools import count

from django.shortcuts import render
from .models import Countries, Employees
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse

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

def orm_list(request):
    employees = Employees.objects.filter(Q(first_name__startswith="A")|
                                         Q(last_name__startswith="B"))
    # employees = Employees.objects.values('first_name', 'last_name')
    print(employees.query)
    employe = ""
    for emp in employees:
        # employe += f"{emp['first_name']} {emp['last_name']} <br>"
        employe += f"{emp.first_name} {emp.last_name} <br>"
    return HttpResponse(employe)