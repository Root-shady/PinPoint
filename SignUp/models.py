# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class SignUp(models.Model):
    # Instead of using Django default field, which name id, specify in the following.
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=30)
    create = models.DateTimeField(auto_now_add=True) #创建日期
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True) #更新日期
    
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'signup'


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100) 
    url = models.URLField(max_length=500) #职位链接
    meta = models.TextField() #其他描述
    description = models.TextField(blank=True) #职位描述
    requirement = models.TextField(blank=True) #职位要求
    plus = models.TextField(blank=True) #加分项
    bonus = models.TextField(blank=True) #福利
    published_date = models.DateTimeField() #发布日期

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'job'

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    job = models.ForeignKey('Job')
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=500)
    location = models.CharField(max_length=50)
    field = models.CharField(max_length=50, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'company'

class Tag(models.Model):
    tag_id = models.PositiveSmallIntegerField() # Values from 0 to 32767
    tag_name = models.CharField(max_length=50)
    job = models.ForeignKey('Job', related_name='job_tag')
    user = models.ForeignKey('SignUp', related_name='user_tag')

    def __str__(self):
        return self.tag_name
    class Meta:
        db_table = 'tag'
