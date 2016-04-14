__author__ = 'ashish'


from django.conf.urls import url,include
from django.contrib import admin
from views import *
from userInfo import userCredentials
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    url(r'^setinfo', setdata, name='setdata'),
    url(r'^getdata', getdata, name='getData'),
    url(r'^signup', userCredentials.signup, name='userSignup'),
    url(r'^pwd', userCredentials.recoverpwd ,name='passwordRecover'),
    url(r'^', userCredentials.login, name='userLogin'),
    url(r'^', home, name='home'),

]

#urlpatterns += staticfiles_urlpatterns()