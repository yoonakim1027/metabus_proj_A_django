# Generated by Django 3.2.12 on 2022-02-07 04:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=100, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('[ㄱ-힣]', message='한글을 입력해주세요.')])),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
