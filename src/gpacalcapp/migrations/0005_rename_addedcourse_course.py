# Generated by Django 5.0 on 2024-02-20 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpacalcapp', '0004_addedcourse_delete_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddedCourse',
            new_name='Course',
        ),
    ]
