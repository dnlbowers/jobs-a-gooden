# Generated by Django 3.2.12 on 2022-03-20 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=400)),
                ('location', models.CharField(max_length=200)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('max_salary', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_expired', models.DateTimeField(blank=True, null=True)),
                ('job_description', models.TextField()),
                ('job_url', models.URLField(max_length=2000)),
                ('status', models.IntegerField(choices=[(0, 'hidden'), (1, 'Public')], default=0)),
                ('is_pinned', models.ManyToManyField(blank=True, related_name='is_pinned', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='PinnedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinned_jobs', models.ManyToManyField(blank=True, related_name='pinned_jobs', to='job_search.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.CharField(max_length=200)),
                ('note', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_insight', models.BooleanField(default=False)),
                ('related_job', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='related_job', to='job_search.job')),
                ('user', models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
