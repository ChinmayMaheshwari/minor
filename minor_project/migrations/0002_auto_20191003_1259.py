# Generated by Django 2.2.5 on 2019-10-03 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minor_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelformwithfile',
            name='user',
            field=models.OneToOneField(default='0', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
