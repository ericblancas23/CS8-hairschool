# Generated by Django 2.0.7 on 2018-07-18 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairschool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='hairschool',
        ),
    ]