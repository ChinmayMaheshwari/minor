# Generated by Django 2.2.6 on 2019-10-14 13:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('minor_project', '0005_auto_20191014_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserWiseInterviewDetails',
            new_name='UserWiseInterviewDetail',
        ),
    ]
