# Generated by Django 4.1.5 on 2023-01-28 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorgu', '0008_remove_news_algo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_score',
        ),
    ]