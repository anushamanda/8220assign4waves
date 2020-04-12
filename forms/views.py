from django.shortcuts import render
from .models import Forms


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def forms(request):
    forms= Forms.objects.all()
    context={
    'forms':forms
    }
    return render(request, 'forms/forms.html', context)

def form(request):
   return render(request, 'forms/form.html')

def search(request):
    return render(request, 'forms/search.html')
