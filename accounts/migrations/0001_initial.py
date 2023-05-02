# Generated by Django 4.1.3 on 2023-05-02 05:17

import accounts.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('cell_phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Start with 09/9 and it must 9 digits after that. For example: 09120000000 or 9120000000', regex='^(09|9)\\d{9}$')], verbose_name='cell_phone')),
                ('avatar', models.ImageField(default='', upload_to='user-avatars', verbose_name='avatar')),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], default=None, max_length=10, null=True, verbose_name='gender')),
                ('national_id', models.CharField(blank=True, max_length=10, null=True, validators=[accounts.validators.validate_national_code], verbose_name='national_id')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_birth', models.DateField(blank=True, null=True, verbose_name='day_of_birth')),
                ('marital_status', models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married')], max_length=10, null=True, verbose_name='marital_status')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.city', verbose_name='city')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last_name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone_number')),
                ('telephone_number', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Start with 09/9 and it must 9 digits after that. For example: 09120000000 or 9120000000', regex='^(09|9)\\d{9}$')], verbose_name='telephone_number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.TextField(verbose_name='address')),
                ('zip_code', models.CharField(max_length=30, verbose_name='zip_code')),
                ('description', models.TextField(verbose_name='description')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.city', verbose_name='city')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
