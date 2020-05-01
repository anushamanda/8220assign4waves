from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect

from .forms import EventForm
from .models import Enrollment

from .models import Event



def landingpage(request):
    return render(request, 'landingpage.html')

@login_required
def home(request):
    current_user = request.user
    if(current_user.is_superuser):
        return render(request, 'landingpage.html')
    elif(current_user.profile.is_customer):
        #parks = Parks.objects.all()
        #context = {'parks': parks}
        return render(request, 'landingpage.html', )
    elif(current_user.profile.is_employee):
        #parks=Parks.objects.all()
        #context = {'parks': parks}
        return render(request, 'landingpage.html',)

def about(request):
    return render(request, 'about.html')


def index(request):
    events = Event.objects.order_by('-list_date').filter(is_published=True)

    paginator= Paginator(events, 10)
    page= request.GET.get('page')
    paged_events= paginator.get_page(page)
    context={
        'events': paged_events
    }
    return render(request, 'events/events.html', context)

def event(request, event_id):
    event= get_object_or_404(Event, pk=event_id)
    context ={
        'event':event
    }
    return render(request, 'events/event.html', context)

def search(request):
    queryset_list = Event.objects.order_by('-list_date')

    # events
    if 'event' in request.GET:
        event = request.GET['event']
        if event:
            queryset_list = queryset_list.filter(event_name__iexact=event)
    context = {
        'events': queryset_list,
        'values': request.GET

    }



    return render(request, 'events/search.html', context)




def enrollment(request):
    if request.method =='POST':
        event_id=request.POST['event_id']
        event = request.POST['event']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        timings = request.POST['timings']
        #advisor_email = request.POST['advisor_email']

        #check if user maede any inquery
        if request.user.is_authenticated:
            user_id=request.user.id
            has_enrolled=Enrollment.objects.all().filter(event_id=event_id, user_id=user_id)
            if has_enrolled:
               messages.error(request, 'You already enrolled in this session')
               return redirect('/events/')

        enrollment= Enrollment(event=event,  name=name, email=email, phone=phone, timings=timings, user_id=user_id, event_id=event_id)
        enrollment.save()


        messages.success(request, 'You are succefully enrolled to this session')
        return redirect('/events/')


def enrolled_events(request):

    user_enrollments = Enrollment.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'enrollments': user_enrollments
    }
    return render(request, 'customerpages/enrolled_events.html', context)



def enrolledevent_delete(request, pk):
   enrollment = get_object_or_404(Enrollment, pk=pk)
   enrollment.delete()
   return redirect ('enrolled_events')

def enrollment_list(request):
    user_enrollments = Enrollment.objects.order_by('-contact_date')
    context = {
        'enrollments': user_enrollments
    }

    return render(request, 'employeepages/enrollment_list.html', context)

@login_required
def event_new(request):
   if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           event = form.save()
           event.save()
           #event.list_date = timezone

           events =Event.objects.all()
           return render(request, 'events/events.html',
                         {'events': events})
   else:
       form = EventForm()
       # print("Else")
   return render(request, 'employeepages/event_new.html', {'form': form})

@login_required
def event_update(request, pk):
   event = get_object_or_404(Event, pk=pk)
   if request.method == "POST":
       form = EventForm(request.POST, instance=event)
       if form.is_valid():
           event = form.save()
           # service.customer = service.id
           event.updated_date = timezone
           event.save()
           events = Event.objects.all()
           return render(request, 'events/events.html', {'events': events})
   else:
       # print("else")
       form = EventForm(instance=event)
   return render(request, 'employeepages/event_update.html', {'form': form})

def event_delete(request, pk):
   customer = get_object_or_404(Event, pk=pk)
   customer.delete()
   return redirect('events')

