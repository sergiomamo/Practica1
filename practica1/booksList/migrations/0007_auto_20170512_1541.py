# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booksList', '0006_auto_20170420_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(default=datetime.date(2017, 5, 12)),
        ),
    ]
