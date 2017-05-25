# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksList', '0010_auto_20170525_1243'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='authorreview',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='booksreview',
            unique_together=set([]),
        ),
    ]
