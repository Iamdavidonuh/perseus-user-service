# Generated by Django 4.0.4 on 2022-04-23 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=35)),
                ('firstName', models.CharField(max_length=35)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('emails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.email')),
                ('phoneNumbers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userservice.phonenumber')),
            ],
        ),
    ]
