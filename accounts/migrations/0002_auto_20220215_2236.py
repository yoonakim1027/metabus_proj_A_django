# Generated by Django 3.2.12 on 2022-02-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password_quiz',
            field=models.CharField(choices=[('내 보물1호는?', '내 보물1호는?'), ('처음 키운 반려동물 이름은?', '처음 키운 반려동물 이름은?'), ('어머니 성함은?', '어머니 성함은?'), ('아버지 성함은?', '아버지 성함은?'), ('좋아하는 음식은?', '좋아하는 음식은?')], default='내 보물1호는?', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(choices=[('서울', '서울'), ('인천', '인천'), ('대전', '대전'), ('세종', '세종'), ('대구', '대구'), ('부산', '부산'), ('광주', '광주'), ('울산', '울산'), ('제주', '제주'), ('강원', '강원')], default='서울', max_length=50),
        ),
    ]
