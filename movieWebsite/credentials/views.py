from django.contrib import auth, messages
from django.http import response
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, AbstractUser
from .forms import ProfileForm


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            # return redirect('login')
            return redirect('credentials:login')
    return render(request,"login.html")

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('credentials:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist")
                return redirect('credentials:register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                messages.info(request, " Congratulations created MovieWeb Successfully,Login here")
                return redirect('credentials:login')
        else:
            messages.info(request,"password not matched")
            return redirect('credentials:register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


# def profile(request):
#     profile_det=User.objects.get(username=request.user)
#     return render(request,"profile.html",{'profile_det':profile_det})

# def profile(request):
#     if request.user.is_authenticated:
#         profile_det=User.objects.filter(request.user)
#     return render(request,"profile.html",{'profile_det':profile_det})


def profile(request,id):
    profile_det=User.objects.get(id=id)
    return render(request,"profile.html")


def update(request,id):
    profile=User.objects.get(id=id)
    form = ProfileForm(request.POST or None, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'editprofile.html', {'forme': form, 'profile': profile})