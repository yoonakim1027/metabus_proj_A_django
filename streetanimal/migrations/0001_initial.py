# Generated by Django 3.2.12 on 2022-02-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_no', models.AutoField(primary_key=True, serialize=False)),
                ('animal_reg_num', models.CharField(max_length=50, unique=True)),
                ('size', models.CharField(choices=[('1', '소형'), ('2', '중형'), ('3', '대형')], default=1, max_length=3)),
                ('sex', models.CharField(choices=[('1', '암컷'), ('2', '수컷')], default=1, max_length=3)),
                ('age', models.IntegerField()),
                ('date_of_discovery', models.DateTimeField()),
                ('place_of_discovery', models.CharField(max_length=30)),
                ('physical_condition', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('protection_status', models.CharField(choices=[('1', '입양 대기'), ('2', '입양 매칭 중'), ('3', '입양 완료!')], default=1, max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SortOfAnimal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
