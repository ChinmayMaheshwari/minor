# Generated by Django 2.2.6 on 2019-10-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minor_project', '0006_auto_20191014_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelformwithfile',
            name='filler_word',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modelformwithfile',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='modelformwithfile',
            name='transcript',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='modelformwithfile',
            name='word_per_minute',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
