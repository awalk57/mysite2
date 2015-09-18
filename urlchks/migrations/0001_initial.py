# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_name', models.CharField(max_length=50)),
                ('agency', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url_text', models.CharField(max_length=250)),
                ('last_check_time', models.DateTimeField(verbose_name=b'last time check')),
                ('last_status_code', models.CharField(max_length=10)),
                ('application_name', models.ForeignKey(to='urlchks.Applications')),
            ],
        ),
    ]
