# Generated by Django 3.2.7 on 2021-09-27 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_createresume_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createresume',
            name='education',
        ),
        migrations.AddField(
            model_name='createresume',
            name='cgpa',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createresume',
            name='college',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createresume',
            name='degree',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createresume',
            name='hsc',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createresume',
            name='ssc',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='createresume',
            name='template',
            field=models.CharField(default=1, max_length=122),
            preserve_default=False,
        ),
    ]
