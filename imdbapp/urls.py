__author__ = 'ashish'


from django.conf.urls import url,include
from django.contrib import admin
from views import *


urlpatterns = [
    url(r'^getinfo', getinfo, name='info'),
    url(r'^$', home, name='home'),

]
