# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20150819_2211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='created_date',
            new_name='start_date',
        ),
    ]
