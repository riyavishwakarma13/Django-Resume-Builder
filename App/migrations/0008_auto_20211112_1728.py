# Generated by Django 3.2.7 on 2021-11-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20211112_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='createresume',
            name='comname1',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='createresume',
            name='comname2',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='createresume',
            name='comname3',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]