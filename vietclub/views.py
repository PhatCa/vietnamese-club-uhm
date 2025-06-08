from django.shortcuts import render
from .models import Landing, Officer, Sponsor, Event
# Create your views here.


def landing_page(request):
    active_event = Event.objects.filter(is_current=True)
    previous_event = Event.objects.filter(is_current=False)
    landing_content = Landing.objects.all()
    officers = Officer.objects.values('name', 'position', 'image_link')
    context = {
        'active_event': active_event,
        'previous_event': previous_event,
        'landing': landing_content,
        'officers': officers
    }
    return render(request, 'base.html', context)


def about_page(request):
    officers = Officer.objects.all()
    sponsors = Sponsor.objects.all()
    context = {
        'officers': officers,
        'sponsors': sponsors
    }

    return render(request, 'about.html', context)


def event_page(request):
    previous_events = Event.objects.filter(
        is_current=False
        ).prefetch_related(
            'sponsors'
            )
    print('www', previous_events)
    context = {
        'previous_events': previous_events
    }
    return render(request, 'event.html', context)
