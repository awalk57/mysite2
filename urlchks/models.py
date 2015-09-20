import datetime
from django.db import models
import django_filters
from django.utils import timezone

# Create your models here.


class Applications(models.Model):
    application_name = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)

    def __unicode__(self):
        return self.application_name


class Urls(models.Model):
    application_name = models.ForeignKey(Applications)
    url_text = models.URLField(max_length=200)
    url_description = models.CharField(max_length=250, blank=True)
    server_list = models.CharField(max_length=200, blank=True)
    last_check_time = models.DateTimeField('last time check', blank=True, auto_now_add=True)
    last_status_code = models.CharField(max_length=10, default='200')

    def __unicode__(self):
        return self.url_text

class ListUrlFilter(django_filters.FilterSet):
    class Meta:
        model = Urls
        fields = {
                'url_text':['icontains'],
                'url_description':['icontains'],
                 }