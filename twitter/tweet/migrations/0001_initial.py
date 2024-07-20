# Generated by Django 5.0.6 on 2024-06-25 15:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('body', models.TextField(max_length=500, verbose_name='Body')),
                ('like_count', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Like_Count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
            ],
        ),
    ]
