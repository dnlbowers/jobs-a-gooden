# Generated by Django 3.2.12 on 2022-02-14 00:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0002_jobsearch_is_pinned'),
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
                ('is_pinned', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('note', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_insight', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PinnedJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_pinned', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_search.job')),
            ],
        ),
        migrations.DeleteModel(
            name='JobSearch',
        ),
        migrations.AddField(
            model_name='notes',
            name='pinned_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_search.pinnedjob'),
        ),
    ]
