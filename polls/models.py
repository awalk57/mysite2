import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

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

