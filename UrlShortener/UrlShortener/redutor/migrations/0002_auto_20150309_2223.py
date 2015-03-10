# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redutor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='url',
            new_name='url_original',
        ),
        migrations.AddField(
            model_name='link',
            name='url_generated',
            field=models.CharField(verbose_name='url gerada', blank=True, max_length=200),
            preserve_default=True,
        ),
    ]
