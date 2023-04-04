# Generated by Django 4.1.3 on 2023-04-04 09:55

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_productcategory_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'verbose_name': 'Coupon', 'verbose_name_plural': 'Coupons'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name': 'Attribute', 'verbose_name_plural': 'Attributes'},
        ),
        migrations.AlterModelOptions(
            name='productattributevalue',
            options={'verbose_name': 'Attribute Value', 'verbose_name_plural': 'Attribute Values'},
        ),
        migrations.AlterModelOptions(
            name='productbrand',
            options={'verbose_name': 'Brand', 'verbose_name_plural': 'Brands'},
        ),
        migrations.AlterModelOptions(
            name='productcatalog',
            options={'verbose_name': 'Catalog', 'verbose_name_plural': 'Catalogs'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='productcomment',
            options={'ordering': ('created_date',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
        migrations.AlterModelOptions(
            name='productquantity',
            options={'verbose_name': 'Product Quantity', 'verbose_name_plural': 'Product Quantities'},
        ),
        migrations.AlterModelOptions(
            name='producttag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
        migrations.AlterModelOptions(
            name='relatedproduct',
            options={'verbose_name': 'Related Product', 'verbose_name_plural': 'Related Products'},
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'verbose_name': 'Seller', 'verbose_name_plural': 'Sellers'},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_amount',
            field=models.PositiveIntegerField(default=0, verbose_name='discount_amount'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_code',
            field=models.CharField(max_length=200, verbose_name='discount_code'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0, verbose_name='discount_percent'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expired_date',
            field=models.DateField(null=True, verbose_name='expired_date'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productbrand', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(upload_to='products', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_alt',
            field=models.CharField(max_length=200, verbose_name='image_alt'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='meta_title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='meta_title'),
        ),
        migrations.AlterField(
            model_name='product',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='upc',
            field=models.CharField(max_length=200, verbose_name='upc'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='product_attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productattribute', verbose_name='product_attribute'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='products',
            field=models.ManyToManyField(to='products.product', verbose_name='products'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='value',
            field=models.CharField(max_length=200, verbose_name='value'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='product-brand-icon', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.productbrand', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='catalog',
            field=models.FileField(upload_to='product-catalogs', verbose_name='catalog'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='productcatalog',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='product-category-icon', verbose_name='icon'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='image_alt',
            field=models.CharField(max_length=200, verbose_name='image_alt'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='meta_description'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='meta_title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='meta_title'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.productcategory', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='is_accepted',
            field=models.BooleanField(default=False, verbose_name='is_accepted'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='products.productcomment', verbose_name='parent'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.FileField(upload_to='', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='productquantity',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.seller', verbose_name='seller'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='producttag',
            name='tag',
            field=models.CharField(max_length=50, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='relatedproduct',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='relatedproduct',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='relatedproduct',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='relatedproduct',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product'),
        ),
        migrations.AlterField(
            model_name='relatedproduct',
            name='related_products',
            field=models.ManyToManyField(related_name='related_products', to='products.product', verbose_name='related_products'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, verbose_name='modified_date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
