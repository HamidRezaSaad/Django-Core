# Generated by Django 4.1.3 on 2023-03-14 09:22

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image_alt_product_meta_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='توضیحات'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='image_alt',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات سئو'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='عنوان سئو'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
