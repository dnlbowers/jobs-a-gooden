# Generated by Django 3.2.13 on 2022-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0014_alter_pinnedjobs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_expired',
            field=models.DateField(blank=True, null=True),
        ),
    ]
