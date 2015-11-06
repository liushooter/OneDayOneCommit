# -*- encoding: utf-8 -*-

from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    url = models.URLField()
    votes = models.IntegerField(default=0)

    class Meta:
        db_table = 'blogs' # 默认的数据库名是 <app_name>_<class_name>, 本例是 blog_blog
