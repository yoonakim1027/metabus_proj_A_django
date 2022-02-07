# Generated by Django 3.2.12 on 2022-02-06 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manageraccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageraccounts.manageracc')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]