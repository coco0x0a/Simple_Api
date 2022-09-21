# Generated by Django 4.1.1 on 2022-09-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField()),
            ],
            options={
                'db_table': 'task',
                'ordering': ['-date_created'],
            },
        ),
    ]