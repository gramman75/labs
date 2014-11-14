# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='block',
            field=models.CharField(default=b'No', max_length=2, choices=[(b'Y', b'Yes'), (b'N', b'No')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='posts',
            name='board',
            field=models.ForeignKey(related_name='posts', to='board.Boards'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='replies',
            name='post',
            field=models.ForeignKey(related_name='replies', to='board.Posts'),
            preserve_default=True,
        ),
    ]
