from django.urls import path, re_path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='tasks'),
    re_path(r'^tasks/name/(?P<name>[a-zA-Z]+)/$', views.task_name, name='task_name'),
    re_path(r'^tasks/number/(?P<number>\d+)/$', views.task_number, name='task_number'),
]
