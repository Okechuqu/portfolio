# Generated by Django 4.1.3 on 2022-12-12 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_profile_timestamp_profile_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
