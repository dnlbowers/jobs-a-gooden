# Generated by Django 3.2.12 on 2022-04-19 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0010_auto_20220418_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='related_job',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_job', to='job_search.job'),
        ),
    ]