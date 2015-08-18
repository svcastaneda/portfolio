# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_auto_20150818_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='pic',
            field=models.URLField(),
        ),
    ]
