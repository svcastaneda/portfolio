# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_activity_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='concentration',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
