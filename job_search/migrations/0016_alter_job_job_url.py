# Generated by Django 3.2.13 on 2022-04-27 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0015_alter_job_date_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_url',
            field=models.SlugField(max_length=2000),
        ),
    ]
