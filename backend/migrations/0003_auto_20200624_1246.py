# Generated by Django 3.0.7 on 2020-06-24 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200624_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='members',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='backend.Backend'),
        ),
    ]