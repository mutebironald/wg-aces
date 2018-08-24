# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-08-21 07:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180816_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='LicenseAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='If you are not the author, enter the name or source here. This is needed for some licenses e.g. the CC-BY-SA.', max_length=60, verbose_name='Author Nane')),
            ],
            options={
                'ordering': ['author_name'],
            },
        ),
        migrations.AlterField(
            model_name='userapi',
            name='creating_user_id',
            field=models.IntegerField(default=1, help_text='Id of the user creating another user         through the application', validators=[django.core.validators.MinValueValidator(1)], verbose_name='Id for user creating '),
        ),
    ]
