# Generated by Django 3.2.12 on 2022-04-17 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_search', '0009_alter_notes_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='notes',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]