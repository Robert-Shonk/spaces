# Generated by Django 4.2.2 on 2023-06-29 02:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_comment_parent_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 2, 16, 24, 178622)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 29, 2, 16, 24, 177993)),
        ),
    ]
