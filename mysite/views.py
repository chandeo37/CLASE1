from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
import datetime

def home(request):

    return render(request, 'home.html')
def contact(request):


    return render(request, 'contact.html')

def about(request):

   return render(request, 'about.html', )

def testimonios(request):
    testimonials = [
        {
            'name': "Maria",
            'testimonio' : "Muy buenoooo"

        },
    {
        'name' : 'Juan',
        'testimonio' : "Muy malo"

    }
    ]
    return render(request, 'testimonios.html', context={'data': testimonials})

