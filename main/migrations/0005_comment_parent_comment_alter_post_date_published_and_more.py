# Generated by Django 4.2.2 on 2023-06-28 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_post_date_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='parent_comment',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 28, 23, 26, 39, 121513)),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
