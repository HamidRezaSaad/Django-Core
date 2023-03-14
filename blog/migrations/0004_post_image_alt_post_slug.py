# Generated by Django 4.1.3 on 2023-03-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_avater_author_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_alt',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
