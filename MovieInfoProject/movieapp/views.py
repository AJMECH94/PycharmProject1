from django.shortcuts import render
from .forms import SignUpForm
from django.http  import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from .models import UserInfo
import requests
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("validation completion")
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'movieapp/signup.html', {'form': form})

@login_required()
def JWT(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data.update({'user': request.user.pk})
        payload = {'username': request.user.username, 'password': request.user.password}
        r = requests.post('http://127.0.0.1:8000/api-token-auth/', params=payload)
        return HttpResponse('Get token auth request and data is as: {}'.format(r.text))


