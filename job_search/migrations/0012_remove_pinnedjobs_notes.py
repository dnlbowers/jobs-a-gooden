# Generated by Django 3.2.12 on 2022-04-22 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0011_alter_notes_related_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinnedjobs',
            name='notes',
        ),
    ]
