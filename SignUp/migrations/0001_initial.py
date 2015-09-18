# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('link', models.URLField(max_length=500)),
                ('location', models.CharField(max_length=50)),
                ('field', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=500)),
                ('meta', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('requirement', models.TextField(blank=True)),
                ('plus', models.TextField(blank=True)),
                ('bonus', models.TextField(blank=True)),
                ('published_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'job',
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'signup',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_id', models.PositiveSmallIntegerField()),
                ('tag_name', models.CharField(max_length=50)),
                ('job', models.ForeignKey(to='SignUp.Job', related_name='job_tag')),
                ('user', models.ForeignKey(to='SignUp.SignUp', related_name='user_tag')),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='job',
            field=models.ForeignKey(to='SignUp.Job'),
        ),
    ]
