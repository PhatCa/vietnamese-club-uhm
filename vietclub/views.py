from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, 'base.html')


def about_page(request):
    return render(request, 'about.html')

def event_page(request):
    return render(request, 'event.html')