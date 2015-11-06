# -*- encoding: utf-8 -*-

from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    url = models.URLField()
    is_publish = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    # http://stackoverflow.com/a/3429915/1240067
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blogs' # 默认的数据库名是 <app_name>_<class_name>, 本例是 blog_blog
