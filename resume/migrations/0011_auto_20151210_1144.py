# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20151210_1046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='graduation',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='accomplishment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='school',
            name='created_date',
        ),
        migrations.AddField(
            model_name='accomplishment',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experience',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='organization',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='school',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
