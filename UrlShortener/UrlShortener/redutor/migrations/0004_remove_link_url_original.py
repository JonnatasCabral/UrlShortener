# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redutor', '0003_auto_20150309_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='url_original',
        ),
    ]
