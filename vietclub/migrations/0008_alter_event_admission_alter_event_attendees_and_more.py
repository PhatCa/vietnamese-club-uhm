# Generated by Django 5.2.1 on 2025-06-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vietclub', '0007_sponsor_sponsor_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='admission',
            field=models.PositiveIntegerField(blank=True, help_text='Specify the cost of admission.Leave blank if the event is free.', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='attendees',
            field=models.PositiveIntegerField(blank=True, help_text='Number of attendees (optional). Leave blank for current events.', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(help_text="The main title of the event, e.g., 'Movie Night'.", max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_sub_name',
            field=models.CharField(help_text="Additional details or subtitle, e.g., 'Mai Movie'.", max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='is_current',
            field=models.BooleanField(help_text='Check this only if the event is current or upcoming.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsors',
            field=models.ManyToManyField(blank=True, help_text='Select sponsors for this event, if any.', related_name='events', to='vietclub.sponsor'),
        ),
    ]
