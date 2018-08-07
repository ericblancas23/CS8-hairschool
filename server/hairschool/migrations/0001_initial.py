# Generated by Django 2.1 on 2018-08-07 00:34

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('Stylist', models.CharField(max_length=30)),
                ('Service', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('styling', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Stylist',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=30)),
                ('availability', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User_Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stylist', models.CharField(max_length=30)),
                ('Service', models.CharField(max_length=30)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Time', models.DateTimeField()),
                ('Consultation', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=3)),
                ('On_time', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=3)),
                ('Styling', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=3)),
                ('Customer_Service', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=3)),
                ('Overall', models.IntegerField(choices=[(1, 'one'), (2, 'two'), (3, 'three')], default=3)),
                ('Notes', models.CharField(max_length=300)),
            ],
        ),
    ]
