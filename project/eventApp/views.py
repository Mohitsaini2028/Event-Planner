from django.shortcuts import render, HttpResponseRedirect
from .models import Event
from .forms import EventForm



def home(request):
    events=Event.objects.all()
    return render(request,"home.html", { 'events':events } )

def addEvent(request):
    form = EventForm()
    context = { 'form':form }
    return render(request,"addEvent.html", context )

def added(request):
    if request.method=='POST':
        form=EventForm(request.POST)
        event= Event()
        event.event_name=form.data['event_name']
        event.data=form.data['data']
        event.location=form.data['location']
        event.time=form.data['time']
        event.image=request.FILES.get('img')
        event.save()

    context = { 'form': form }
    return HttpResponseRedirect('/')

def like(request):
    if request.method=='POST':
        eventId=int(request.POST['eventId'])
        event = Event.objects.get(id=eventId)
        event.is_liked=True
        event.save()
    return HttpResponseRedirect('/')

def unlike(request):
    if request.method=='POST':
        eventId=int(request.POST['eventId'])
        event = Event.objects.get(id=eventId)
        event.is_liked=False
        event.save()
    return HttpResponseRedirect('/')
