# Generated by Django 4.0.6 on 2022-11-04 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, unique=True),
        ),
    ]
