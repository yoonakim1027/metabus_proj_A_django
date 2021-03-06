# Generated by Django 3.2.12 on 2022-02-27 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notice_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image1', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('image2', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('image3', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('image4', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('image5', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('file1', models.FileField(blank=True, upload_to='')),
                ('file2', models.FileField(blank=True, upload_to='')),
                ('file3', models.FileField(blank=True, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-notice_no'],
            },
        ),
    ]
