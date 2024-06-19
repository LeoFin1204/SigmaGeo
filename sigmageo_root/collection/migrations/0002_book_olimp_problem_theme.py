# Generated by Django 5.0.4 on 2024-05-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('chapters', models.TextField(default='[]')),
            ],
        ),
        migrations.CreateModel(
            name='Olimp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('stages', models.TextField(default='[]')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('num', models.SmallIntegerField(default=0)),
                ('grade', models.CharField(max_length=5)),
                ('text', models.TextField()),
                ('solution', models.TextField(default='')),
                ('themes', models.TextField(default='[]')),
                ('source', models.CharField(default='', max_length=250)),
                ('year', models.SmallIntegerField(null=True)),
                ('stage', models.CharField(default='', max_length=150)),
                ('author', models.CharField(default='', max_length=150)),
                ('dif', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(null=True)),
                ('edu_tasks', models.TextField(default='[]')),
            ],
        ),
    ]
