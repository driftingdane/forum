# Generated by Django 4.1.1 on 2022-10-01 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0018_alter_forum_options_forum_cat_slug_forum_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='claps',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
