# Generated by Django 4.1.3 on 2022-12-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_skills_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
