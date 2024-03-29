# Generated by Django 4.1.3 on 2022-12-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_skills_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Skill_3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill_1',
        ),
    ]
