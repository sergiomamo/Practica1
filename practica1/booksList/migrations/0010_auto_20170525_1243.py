# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booksList', '0009_auto_20170522_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='date',
            field=models.DateTimeField(default=datetime.date(2017, 5, 25)),
        ),
        migrations.AlterUniqueTogether(
            name='authorreview',
            unique_together=set([('author', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='booksreview',
            unique_together=set([('books', 'user')]),
        ),
    ]
