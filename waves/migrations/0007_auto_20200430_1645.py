# Generated by Django 2.2.6 on 2020-04-30 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0006_enrollment_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='timings',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
