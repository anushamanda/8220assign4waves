# Generated by Django 2.2.6 on 2020-04-30 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0007_auto_20200430_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='event_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
