# Generated by Django 3.0.7 on 2020-06-24 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ok', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('real_name', models.CharField(max_length=30)),
                ('tz', models.CharField(max_length=40)),
                ('members', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='backend.Backend')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('members', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='backend.Users')),
            ],
            options={
                'ordering': ['start_time'],
                'unique_together': {('start_time', 'end_time')},
            },
        ),
    ]
