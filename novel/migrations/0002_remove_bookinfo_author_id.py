# Generated by Django 5.0.1 on 2024-01-13 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinfo',
            name='author_id',
        ),
    ]
