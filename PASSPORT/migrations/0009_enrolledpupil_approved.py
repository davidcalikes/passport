# Generated by Django 3.2.15 on 2022-09-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PASSPORT', '0008_alter_enrolledpupil_pupil_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolledpupil',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]