from django.urls import path
from .views import orm_list

urlpatterns = [
    path('orm-list/', orm_list, name='orm_list'),
]