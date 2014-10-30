# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, choices=[(b'A', b'\xec\x9d\xbc\xeb\xb0\x98'), (b'B', b'\xea\xb2\xbd\xec\xa0\x9c'), (b'C', b'\xec\x97\xb0\xec\x98\x88 ')])),
                ('title', models.CharField(max_length=240)),
                ('comment', models.TextField()),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField(null=True)),
                ('enabled', models.CharField(default=b'N', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=240)),
                ('contents', models.TextField()),
                ('block', models.CharField(default=b'N', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('group', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('seq', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('level', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('board', models.ForeignKey(to='board.Boards')),
                ('createdBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contents', models.TextField()),
                ('block', models.CharField(default=b'N', max_length=1, choices=[(b'Y', b'Yes'), (b'N', b'No')])),
                ('group', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('seq', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('level', models.DecimalField(max_digits=100000, decimal_places=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='board.Posts')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
