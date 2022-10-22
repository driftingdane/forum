# Generated by Django 4.1.1 on 2022-09-12 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=250, null=True, unique=True, unique_for_date='publish'),
        ),
    ]