# Generated by Django 4.2.2 on 2023-06-28 23:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_parent_comment_alter_post_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 28, 23, 28, 41, 415037)),
        ),
    ]
