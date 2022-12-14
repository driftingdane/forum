# Generated by Django 4.1.1 on 2022-09-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_alter_discussion_forum'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forum',
            options={'get_latest_by': ['-created'], 'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='forum',
            name='cat_slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='forum',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
