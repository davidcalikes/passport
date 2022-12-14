# Generated by Django 3.2.15 on 2022-09-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0013_profile_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='my_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
