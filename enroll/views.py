from django.shortcuts import render
from .forms import StudentRegistration
from  django.http import HttpResponseRedirect
from .models import User
# Create your views here.


def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration()
            return HttpResponseRedirect('/')
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})



def delete_data(request,id):
        data=User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')



def update_data(request,id):
    if request.method=="POST":
        obj=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=obj)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        obj=User.objects.get(pk=id)
        fm=StudentRegistration(instance=obj)
        return render(request, 'enroll/updatestudent.html',{'form':fm})


