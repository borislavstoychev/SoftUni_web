# Generated by Django 3.2.3 on 2021-06-08 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_like_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='test',
        ),
    ]