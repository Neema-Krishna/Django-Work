# Generated by Django 4.2.5 on 2023-10-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0011_rename_message_query_subject_query_your_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='query',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]