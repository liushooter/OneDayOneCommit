# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 16, 52, 53, 236555, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 16, 53, 6, 850105, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
