# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20150818_0654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='linkalt',
            new_name='alt',
        ),
    ]
