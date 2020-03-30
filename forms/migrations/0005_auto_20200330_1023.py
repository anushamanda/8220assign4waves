# Generated by Django 3.0.4 on 2020-03-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_record_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forms',
            name='form_1',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='form_2',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='form_3',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='form_4',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='record_log',
            name='upload_form',
            field=models.FileField(blank=True, upload_to='uploadedfiles/%Y/%m/%d/'),
        ),
    ]
