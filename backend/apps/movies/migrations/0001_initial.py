# Generated by Django 4.2.5 on 2023-11-23 06:46

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('trailer_link', models.CharField(max_length=300, verbose_name='trailer')),
                ('rating', models.FloatField(blank=True, null=True, verbose_name='rating')),
                ('movie_duration', models.IntegerField(default=45, verbose_name='duration')),
                ('state', models.CharField(default='USA', max_length=50, verbose_name='state')),
                ('release_type', models.CharField(choices=[('Newly Released', 'Newly Released'), ('Upcoming', 'Upcoming')], max_length=50, verbose_name='release_type')),
                ('release_date', models.IntegerField(verbose_name='release date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Datetime')),
            ],
        ),
    ]
