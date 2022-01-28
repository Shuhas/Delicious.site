# Generated by Django 4.0.1 on 2022-01-27 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('steps', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('prep', models.IntegerField()),
                ('cook', models.IntegerField()),
                ('yields', models.IntegerField()),
                ('rate', models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')])),
                ('img', models.ImageField(upload_to='')),
                ('ctg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.category')),
            ],
        ),
    ]