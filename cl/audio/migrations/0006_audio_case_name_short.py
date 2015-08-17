# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0005_auto_20150807_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='case_name_short',
            field=models.TextField(help_text=b"The abridged name of the case, often a single word, e.g. 'Marsh'", blank=True),
        ),
    ]
