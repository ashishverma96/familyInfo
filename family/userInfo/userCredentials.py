from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordResetForm
# Create your views here.

from ..models import UserInfo
from ..forms import UserSignUpform
from ..forms import loginform


def signup(request):
    if request.method == "GET":
        signup_form = UserSignUpform()
        return render(request, 'sign_up.html',{
            'form': signup_form})


    if request.method == "POST":
        form = UserSignUpform(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return HttpResponse("Username already exist")
            else:
                user = User.objects.create_user(username=form.cleaned_data['username'],email=form.cleaned_data['email']\
                           ,password=form.cleaned_data['password'])
                return render(request, 'log_in.html')


def login(request):
    if request.method == "GET":
        login_form = loginform()
        return render(request, 'log_in.html', {
            'form': login_form})

    if request.method == "POST":


        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            return  render_to_response('family_get.html')
        else:
            return  HttpResponse("No user")


def recoverpwd(request):
    if request.method == "GET":
        return render(request,'password_recovery.html')

    if request.method == "POST":
        form = PasswordResetForm({'username': 'ashish'})
        print ("Username is",request.POST['username'])


        x = send_mail('Subject here', 'Here is the message.', 'akumarlpu@gmail.com',
                      ['averma@loggly.com'])
        return HttpResponse("Username already exist")
