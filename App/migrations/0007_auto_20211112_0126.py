# Generated by Django 3.2.7 on 2021-11-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_auto_20211112_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createresume',
            name='j1ed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createresume',
            name='j1sd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createresume',
            name='j2ed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createresume',
            name='j2sd',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createresume',
            name='j3ed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createresume',
            name='j3sd',
            field=models.DateField(blank=True, null=True),
        ),
    ]
