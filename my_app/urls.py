from django.urls import path
from .views import index_page, get_max_salary_employess, get_dependents, register

urlpatterns = [
    path('', index_page, name='index_page'),
    path('max-salary/<int:top>', get_max_salary_employess, name='max-salary-employees'),
    path('deps/<int:employee_id>', get_dependents, name='deps-list'),
    path('register/', register, name='register'),
]