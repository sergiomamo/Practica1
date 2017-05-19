# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booksList', '0007_auto_20170512_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.ForeignKey(default=1, to='booksList.Author'),
        ),
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(default=datetime.date(2017, 5, 19)),
        ),
    ]
