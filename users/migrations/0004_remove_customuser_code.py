# Generated by Django 3.2.19 on 2023-07-03 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='code',
        ),
    ]