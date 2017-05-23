# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booksList', '0008_auto_20170519_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='nacionalidad',
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='state',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='country',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(default=datetime.date(2017, 5, 22)),
        ),
    ]
