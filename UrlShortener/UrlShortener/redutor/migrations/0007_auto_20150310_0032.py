# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redutor', '0006_auto_20150309_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url_original',
            field=models.URLField(verbose_name='original'),
            preserve_default=True,
        ),
    ]
