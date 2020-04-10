from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

def forms(request):
   return render(request, 'forms/forms.html')

def form(request):
   return render(request, 'forms/form.html')

def search(request):
    return render(request, 'forms/search.html')
