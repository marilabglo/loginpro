from newloginapp.models import students,marksheet
from django.shortcuts import render
from django.http import HttpResponse
from newloginapp.forms import studentform,markform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth.forms import  AuthenticationForm

from django.contrib import messages








def login_user(request):
   
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
               
                login(request, user)
                return HttpResponse("login successfully")
                #return redirect("listview")
            else:
                pass
               
        else:
            messages.error(request, ("please enter your username and password"))
    form=AuthenticationForm()
    return render(request, 'login.html', {'form': form})             
            


@login_required
def add(request):
    gett = studentform(request.POST or None, request.FILES or None)
    if gett.is_valid():
       gett.save()
    else:
        pass
    return render(request,"stform.html",{'form':gett})
@login_required
def addmarks(request,id):
    datas= marksheet.objects.filter(id=id).values()
    obj = markform(request.POST or None)
    if obj.is_valid():
        cb=obj.save(commit=False)
        cb.created_by=(request.user).username
        cb.save()
    return render(request,"markadd.html",{'obj':obj})

@login_required
def listview(request):
    datas = students.objects.all()
    context={'datas':datas}
    return render(request, "listview.html", context)
@login_required    
def viewdetails(request):
    datas= marksheet.objects.filter().values()
    
    context={'datas':datas}
    return render(request, "marksheet.html", context)
@login_required
def edit(request, id):
    obj = marksheet.objects.get(id = id)
    form = markform(request.POST or None, instance = obj)
    if form.is_valid():
        f=form.save(commit=False)
        f.updated_by=(request.user).username
        f.save()
    context={'form': form}
    return render(request, "edit.html", context)
from django.http import JsonResponse


def jsondata(request):
	data = list(marksheet.objects.values())
	return JsonResponse(data,safe = False)
	
	


      
    
    

            
            


    
   
   

# Create your views here.
