# Generated by Django 4.1.5 on 2023-01-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorgu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_Subject',
            field=models.CharField(default='a', max_length=50),
        ),
        migrations.AddField(
            model_name='news',
            name='news_score',
            field=models.DecimalField(decimal_places=7, default='0.00', max_digits=9),
        ),
    ]
