# Generated by Django 3.2.12 on 2022-02-09 11:01

import accounts.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('userID', models.CharField(max_length=18, primary_key=True, serialize=False, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(help_text='입력 예) 042-1234-1234', max_length=16, validators=[django.core.validators.RegexValidator('^\\d{3}-?\\d{4}-?\\d{4}$', message='전화번호를 입력해주세요.')])),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('region', models.CharField(choices=[('1', 'Seoul'), ('2', 'Busan'), ('3', 'Daegu'), ('4', 'Incheon'), ('5', 'Daejeon'), ('6', 'Sejong'), ('7', 'Gwangju'), ('8', 'Ulsan'), ('9', 'Jeju'), ('10', 'Gangwon')], default=1, max_length=7)),
                ('password_quiz', models.CharField(choices=[('1', '내 보물1호는?'), ('2', '처음 키운 반려동물 이름은?'), ('3', '어머니 성함은?'), ('4', '아버지 성함은?'), ('5', '좋아하는 음식은?')], default=1, max_length=1)),
                ('password_quiz_answer', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
