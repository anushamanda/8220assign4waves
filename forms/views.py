from django.shortcuts import render
from .models import Forms, Uploadforms



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

def uploadforms(request):
    uploadforms = Uploadforms.objects.all()
    context = {
        'uploadforms': uploadforms
    }
    return render(request, 'forms/uploadforms.html', context)


def search(request):
    return render(request, 'forms/search.html')

def home(request):
    current_user = request.user
    if(current_user.is_superuser):
        return render(request, 'pages/index.html')
    elif(current_user.profile.is_supervisor):
        return render(request, 'supervisor/supervisordash.html')
    elif(current_user.profile.is_firefighter):
        return render(request, 'pages/index.html')

