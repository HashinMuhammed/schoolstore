from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib import messages
from .forms import StudentForm
from . models import Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('schoolapp:index')
        else:
            messages.info(request,"invalid")
            return redirect('/login')


    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:  
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
            messages.info(request,"user created")
        else:
            messages.info(request,'password not matching')
            return redirect('/register')
        return redirect('/login')

    return render(request, 'register.html')

def new(request):
    return render(request,"new.html")

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

@login_required
def submitForm(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order Confirmed')
            return redirect('/new')
    context = {
        'form': form,
    }
    return render(request,'form.html',context)

def load_cities(request):
    department_id = request.GET.get('department_id')
    course = Course.objects.filter(department_id=department_id)
    return render(request, 'citydropdown.html', {'course': course})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)