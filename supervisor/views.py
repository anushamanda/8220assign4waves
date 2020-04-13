from django.shortcuts import render

# Create your views here.


def super_dash(request):
    return render(request, 'supervisor/super_dash.html')
