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
            name='JobTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.ForeignKey(related_name='job_t', to='SignUp.Job')),
            ],
            options={
                'db_table': 'jobtag',
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
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(serialize=False, primary_key=True)),
                ('tag_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
        migrations.CreateModel(
            name='UserTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.ForeignKey(related_name='tag_i', to='SignUp.Tag')),
                ('user', models.ForeignKey(related_name='user_t', to='SignUp.SignUp')),
            ],
            options={
                'db_table': 'usertag',
            },
        ),
        migrations.AddField(
            model_name='signup',
            name='tag',
            field=models.ManyToManyField(to='SignUp.Tag', through='SignUp.UserTag'),
        ),
        migrations.AddField(
            model_name='jobtag',
            name='tag',
            field=models.ForeignKey(related_name='tag_t', to='SignUp.Tag'),
        ),
        migrations.AddField(
            model_name='job',
            name='tag',
            field=models.ManyToManyField(to='SignUp.Tag', through='SignUp.JobTag'),
        ),
        migrations.AddField(
            model_name='company',
            name='job',
            field=models.ForeignKey(to='SignUp.Job'),
        ),
        migrations.AlterUniqueTogether(
            name='usertag',
            unique_together=set([('user', 'tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='jobtag',
            unique_together=set([('job', 'tag')]),
        ),
    ]
