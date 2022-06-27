from rest_framework.views import APIView
from django.shortcuts import render,redirect,reverse
from rest_framework.response import Response
from .serializers import UserSerializer
from .forms import UserForm
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,"users/home.html")

def register_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return redirect('/')
    return render(request, "users/signup.html", {'form':form})


class RegisterView(APIView):
    def post(self,request):
        ser = UserSerializer(request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data)
