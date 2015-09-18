import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Applications(models.Model):
    application_name = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)

    def __unicode__(self):
        return self.application_name


class Urls(models.Model):
    application_name = models.ForeignKey(Applications)
    url_text = models.CharField(max_length=250)
    last_check_time = models.DateTimeField('last time check')
    last_status_code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.url_text
