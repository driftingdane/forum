# Generated by Django 4.1.1 on 2022-09-18 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_alter_discussion_slug_alter_discussion_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
    ]
