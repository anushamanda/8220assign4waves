# Generated by Django 2.2.6 on 2020-04-29 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='is_firefighter',
            new_name='is_customer',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='is_supervisor',
            new_name='is_employee',
        ),
    ]