# Generated by Django 2.2.6 on 2020-04-30 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waves', '0005_remove_enrollment_enroll_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='timings',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
