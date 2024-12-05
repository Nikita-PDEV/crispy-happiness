# Generated by Django 5.1.4 on 2024-12-04 16:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('other_titles', models.TextField(blank=True, null=True)),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], max_length=20)),
                ('coord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pereval.coords')),
            ],
        ),
    ]