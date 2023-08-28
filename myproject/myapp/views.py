from django.shortcuts import render
from django.http import HttpResponse

def task_list(request):
    return HttpResponse("TASK LIST")

def task_name(request, name):
    return HttpResponse(f"Name of task in list: {name}")

def task_number(request, number):
    return HttpResponse(f"The number of task is: №{number}")
