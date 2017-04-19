# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
                ('age', models.IntegerField()),
                ('country', models.TextField(max_length=50)),
                ('nacionalidad', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('author', models.TextField(max_length=50)),
                ('date', models.DateTimeField()),
                ('editorial', models.TextField(max_length=50)),
                ('rating', models.IntegerField()),
                ('reviews', models.IntegerField()),
                ('genere', models.TextField(max_length=50)),
                ('numPages', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(max_length=50)),
            ],
        ),
    ]
