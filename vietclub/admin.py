from django.contrib import admin
from .models import Landing, Officer, Sponsor, Event

# Register your models here.
admin.site.register(Landing)
admin.site.register(Officer)
admin.site.register(Sponsor)
admin.site.register(Event)