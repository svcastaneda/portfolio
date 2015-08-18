# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20150818_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.CharField(max_length=500),
        ),
    ]
