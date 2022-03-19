# Generated by Django 3.2.12 on 2022-03-19 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_search', '0002_auto_20220319_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='related_job',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='job_search.job'),
        ),
        migrations.AddField(
            model_name='notes',
            name='user',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
