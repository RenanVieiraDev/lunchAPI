# Generated by Django 3.2.6 on 2021-08-20 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunch', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='menu',
            new_name='menuSegunda',
        ),
    ]
