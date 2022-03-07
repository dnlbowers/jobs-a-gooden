# Generated by Django 3.2.12 on 2022-03-07 01:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_search', '0008_job_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='is_pinned',
        ),
        migrations.RemoveField(
            model_name='pinnedjob',
            name='date_pinned',
        ),
        migrations.AddField(
            model_name='pinnedjob',
            name='is_pinned',
            field=models.ManyToManyField(blank=True, related_name='pinned_job', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pinnedjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
