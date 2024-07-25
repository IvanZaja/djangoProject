# Generated by Django 5.0.7 on 2024-07-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='No title provided', max_length=50),
        ),
    ]
