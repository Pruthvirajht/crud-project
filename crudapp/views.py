from django.shortcuts import render
from .foms import StudentRegistration
from .models import User
from django.http import HttpResponseRedirect

# This Fuction add and show the data to User

def add(request):
    if request.method == 'POST':
        fm =StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
        stud = User.objects.all()
    return render(request,'add.html',{'form':fm,'stu':stud})

#THis Function is update and edut

def update(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi) 
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi) 
    return render(request,'update.html',{'form':fm})






def delete(request,id):
    if request.method == 'POST':
        ed = User.objects.get(pk=id)
        ed.delete()
        return HttpResponseRedirect('/')
