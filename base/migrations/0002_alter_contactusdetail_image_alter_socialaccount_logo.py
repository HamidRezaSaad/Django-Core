# Generated by Django 4.1.3 on 2023-05-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusdetail',
            name='image',
            field=models.FileField(upload_to='contact_us', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='logo',
            field=models.FileField(upload_to='social_accounts', verbose_name='logo'),
        ),
    ]
