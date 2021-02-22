# Generated by Django 3.0.5 on 2021-02-22 19:43

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'username already exists.'}, max_length=30, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.TextField(choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin'), ('django_admin', 'Django Admin')], default='user')),
                ('bio', models.TextField(null=True, verbose_name='О себе')),
            ],
            options={
                'ordering': ['-id'],
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
