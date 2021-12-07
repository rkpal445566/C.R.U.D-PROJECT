from django.http import request
from django.shortcuts import render,HttpResponseRedirect
from app_1.models import User
from .forms import Student

# Create your views here. RENDER HTML FIELS or this function create ana show data
def showdata(request):
    if request.method =='POST':
      RK=Student(request.POST)
      if RK.is_valid():
       nm=RK.cleaned_data['name']
       em=RK.cleaned_data['email']
       pw=RK.cleaned_data['password']
       reg =User(name=nm, email=em , password=pw)
       reg .save()


       RK=Student()
    else:
       RK=Student() # give the blanck forms 
    stud1 = User.objects.all() #this method display on dat
    return render(request,'app_1/showform.html', {'var1':RK, 'stu':stud1})

   
   
def ubdate_data(request,id):
   if request.method=='POST':
      pi=User.objects.get(pk=id)
      fn=Student(request.POST, instance=pi)
      
      if fn.is_valid():
         fn.save()
   else:
      pi=User.objects.get(pk=id)
      fn=Student(instance=pi)
   
   return render (request, 'app_1/ubdate.html',{'id':fn})   
   
   
   
    # this function is delete

def delete_data(request,id):      #dynamic data are come in id 
  if request.method=='POST':
   pi = User.objects .get(pk=id)
   pi.delete()
  return  HttpResponseRedirect('/')
