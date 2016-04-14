from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.views.generic import View
from forms import InfoForm
#class class_imdb(View):
def home(request):


    print "In Main File"

    form_class = InfoForm

    return render(request, 'imdbform.html', {
        'form': form_class,
    })


def getinfo(request):

    print request
    form = InfoForm(request.POST)
    if form.is_valid():
        print "In new File"
    else:
        print "Wrong Form"



