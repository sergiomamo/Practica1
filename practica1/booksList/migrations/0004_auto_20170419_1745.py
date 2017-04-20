# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booksList', '0003_auto_20170419_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveSmallIntegerField(default=3, verbose_name='Rating (stars)', choices=[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')])),
                ('comment', models.TextField(null=True, blank=True)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('isbn', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('editorial', models.TextField(max_length=50)),
                ('rating', models.IntegerField()),
                ('reviews', models.IntegerField()),
                ('genere', models.TextField(max_length=50)),
                ('numPages', models.IntegerField()),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='bookreview',
            name='books',
            field=models.ForeignKey(to='booksList.Books'),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
