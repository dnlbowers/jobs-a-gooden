# Generated by Django 3.2.13 on 2022-04-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0016_alter_job_job_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_url',
            field=models.URLField(max_length=2000),
        ),
    ]
