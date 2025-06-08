from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


class Landing(models.Model):
    landing_img_link = models.URLField(max_length=500)
    current_total_club_member = models.PositiveIntegerField()

    def clean(self):
        if not self.pk and Landing.objects.exists():
            raise ValidationError("Only one Landing entry is allowed. Please edit the existing one")


class Officer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=60)
    about = models.TextField()
    image_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    image_link = models.URLField()
    sponsor_link = models.URLField()

    def __str__(self):
        return self.name


class Event(models.Model):
    event_name = models.CharField(
        max_length=100,
        help_text="The main title of the event, e.g., 'Movie Night'."
        )
    event_sub_name = models.CharField(
        max_length=100,
        help_text="Additional details or subtitle, e.g., 'Mai Movie'."
        )
    event_description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    admission = models.PositiveIntegerField(null=True, blank=True,
                                            help_text=(
                                                "Specify the "
                                                "cost of admission."
                                                "Leave blank if the "
                                                "event is free."
                                            )
                                            )
    is_current = models.BooleanField(help_text=("Check this only if the event "
                                                "is current or upcoming."))
    attendees = models.PositiveIntegerField(null=True, blank=True, help_text=(
        "Number of attendees (optional). Leave blank for current events."
        ))
    image_link = models.URLField()
    reservation_form_link = models.URLField()
    sponsors = models.ManyToManyField(
        'Sponsor', related_name='events', blank=True, help_text=(
            "Select sponsors for this event, if any."
            )
        )

    def __str__(self):
        return self.event_name

    def clean(self):
        if self.is_current and self.attendees:
            raise ValidationError(
                "If the Event is current then you cannot give attendees"
                )
