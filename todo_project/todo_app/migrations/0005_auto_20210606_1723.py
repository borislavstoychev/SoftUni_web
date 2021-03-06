# Generated by Django 3.2.4 on 2021-06-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20210606_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='stat_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home stuff'), ('Work stuff', 'Work stuff')], max_length=20),
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
