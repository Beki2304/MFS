# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Odgovor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('naslednje_vprasanje', models.ForeignKey(to='blog.Vprasanje', related_name='prejsnja_vprasanja')),
                ('vprasanje', models.ForeignKey(to='blog.Vprasanje')),
            ],
        ),
    ]
