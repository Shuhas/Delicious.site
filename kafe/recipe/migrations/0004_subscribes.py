# Generated by Django 4.0.1 on 2022-01-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_suggestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subs_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
