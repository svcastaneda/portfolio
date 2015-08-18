# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.utils.timezone
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resume', '0002_project_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default=datetime.datetime(2015, 8, 18, 6, 54, 40, 839257, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='linkalt',
            field=models.CharField(default=datetime.datetime(2015, 8, 18, 6, 54, 48, 255655, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='pic',
            field=models.URLField(default=datetime.datetime(2015, 8, 18, 6, 54, 55, 288026, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='published_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
