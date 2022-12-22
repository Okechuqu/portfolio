# Generated by Django 4.1.3 on 2022-12-12 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='profile',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]