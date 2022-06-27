from django.shortcuts import render,redirect,reverse
from .forms import *
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required
import datetime
import jwt

def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        #new_user = authenticate(username=user.username, password=password)
        #login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/')

    context = {'form': form,}
    return render(request, "testapp/signup.html", context)


@login_required(login_url='login/')
def home(request):
    return render(request,"testapp/home.html")

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secrate', algorithm='HS256').decode('utf-8')
        return render(request, "testapp/home.html", {'JWTTOKEN':token})
        if next:
            return redirect(next)
        return redirect('/')
    return render(request, "testapp/login.html", {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')
