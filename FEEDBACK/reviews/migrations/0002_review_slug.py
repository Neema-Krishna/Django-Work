# Generated by Django 4.2.5 on 2023-09-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
