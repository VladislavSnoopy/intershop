# Generated by Django 3.2.4 on 2021-10-13 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='price',
        ),
    ]