from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
# Create your views here.
from forms import familyform
from models import UserInfo


@login_required
def setdata(request):
    if request.method == "GET":
        family_form = familyform()
        return render(request, 'family_setData.html', {
            'form': family_form})

    if request.method == "POST":
        print "In SET DAATA"
        form = familyform(request.POST)
        form.errors
        if form.is_valid():
            print "Form is valid"
            f_info = UserInfo(name=form.cleaned_data['name'], age=form.cleaned_data['age'],
                              phone_no=form.cleaned_data['phone_no'])
            f_info.save()
            return HttpResponse("Data Entered successfully")
        else:
            print "Data is not entered"
            return HttpResponse("Please provide Correct data")



def home(request):
    response = render(request, "sign_up.html")
    return response

def not_found(request):
    print "in this"
    response = render(request, "404.html")
    response.status_code = 404
    return response

@login_required
def getdata(request):
    if request.method == "GET":
        print "In get Data"
        return render(request, 'family_get.html')
    if request.method == "POST":
        print "RequestedURL is ",request.POST['name']
        x = UserInfo.objects.get(name = request.POST['name'])
        print x

