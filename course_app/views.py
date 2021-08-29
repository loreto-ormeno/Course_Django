from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.

def courses(request):
    context = {
        'course':Course.objects.all(),
    }
    return render(request,'course_app/courses.html',context)

def redirecto(request):
    context = {
        'course':Course.objects.all(),
    }
    return render(request,'course_app/courses.html',context)

def create(request):
    if request.method == 'GET':
            return redirect('/')
    elif request.method == 'POST':
        errors = Course.objects.field_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/') 
        else:
            name = request.POST['name']
            desc = request.POST['desc']
            obj = Course.objects.create(name=name, desc=desc)
            obj.save()
            return redirect('/')

def destroy(request, course_id):
    context = {
        'course':Course.objects.get(id=course_id)
    }
    return render(request, 'course_app/destroy.html', context)    


def remove(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')