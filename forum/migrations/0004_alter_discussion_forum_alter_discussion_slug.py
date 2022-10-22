# Generated by Django 4.1.1 on 2022-09-18 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_discussion_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='forum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='slug',
            field=models.SlugField(allow_unicode=True, choices=[('noslug', 'Noslug'), ('haveslug', 'Haveslug')], max_length=250, null=True, unique=True, unique_for_date='publish'),
        ),
    ]