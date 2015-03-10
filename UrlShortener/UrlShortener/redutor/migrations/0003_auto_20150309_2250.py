# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redutor', '0002_auto_20150309_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url_generated',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
