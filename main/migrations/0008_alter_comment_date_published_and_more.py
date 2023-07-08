# Generated by Django 4.2.2 on 2023-07-08 00:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_comment_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 8, 0, 37, 46, 898104)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 7, 8, 0, 37, 46, 896094)),
        ),
        migrations.CreateModel(
            name='PostUpvote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostHelpful',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostFunny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostDownvote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.post')),
            ],
        ),
    ]