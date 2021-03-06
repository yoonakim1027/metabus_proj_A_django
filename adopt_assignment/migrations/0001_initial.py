# Generated by Django 3.2.12 on 2022-02-27 20:45

import adopt_assignment.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('streetanimal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdoptAssignment',
            fields=[
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('assignment_no', models.AutoField(primary_key=True, serialize=False)),
                ('adopter_name', models.CharField(db_index=True, max_length=30)),
                ('monthly_income', models.IntegerField()),
                ('residential_type', models.CharField(choices=[('아파트', '아파트'), ('빌라', '빌라'), ('주택', '주택'), ('원룸', '원룸'), ('오피스텔', '오피스텔')], default='아파트', max_length=50)),
                ('have_pet_or_not', models.BooleanField()),
                ('picture_of_residence1', models.ImageField(upload_to='', validators=[adopt_assignment.models.validate_image])),
                ('picture_of_residence2', models.ImageField(upload_to='', validators=[adopt_assignment.models.validate_image])),
                ('picture_of_residence3', models.ImageField(upload_to='', validators=[adopt_assignment.models.validate_image])),
                ('place_to_meet', models.CharField(choices=[('서울 강동구청 반려동물팀', '서울 강동구청 반려동물팀'), ('대전 동물 보호 센터', '대전 동물 보호 센터'), ('세종 유기동물 보호센터', '세종 유기동물 보호센터'), ('대구 유기동물 보호 협회', '대구 유기동물 보호 협회'), ('부산 동물보호센터', '부산 동물보호센터')], default='서울 강동구청 반려동물팀', max_length=100)),
                ('date_to_meet', models.DateField()),
                ('status', models.CharField(choices=[('신청', '신청'), ('심사 중', '심사 중'), ('수락', '수락'), ('교육 중', '교육 중'), ('입양 완료', '입양 완료'), ('거절', '거절')], db_index=True, default='신청', max_length=50)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='streetanimal.animal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-assignment_no'],
            },
        ),
    ]
