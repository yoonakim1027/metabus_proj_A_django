from django.conf import settings
from django.db import models

from accounts.models import User
from streetanimal.models import Animal


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdoptAssignment(TimestampedModel):
    assignment_no = models.AutoField(primary_key=True)
    adopter_name = models.CharField(max_length=30, db_index=True)
    monthly_income = models.IntegerField()
    residential_type = models.CharField(max_length=50, choices=[
        ("아파트", "아파트"),
        ("빌라", "빌라"),
        ("주택", "주택"),
        ("원룸", "원룸"),
        ("오피스텔", "오피스텔"),
    ], default="아파트")
    have_pet_or_not = models.BooleanField()
    picture_of_residence1 = models.ImageField()
    picture_of_residence2 = models.ImageField()
    picture_of_residence3 = models.ImageField()
    place_to_meet = models.CharField(max_length=100, choices=(
        ("서울 강동구청 반려동물팀", "서울 강동구청 반려동물팀"),
        ("대전 동물 보호 센터", "대전 동물 보호 센터"),
        ("세종 유기동물 보호센터", "세종 유기동물 보호센터"),
        ("대구 유기동물 보호 협회", "대구 유기동물 보호 협회"),
        ("부산 동물보호센터", "부산 동물보호센터"),
    ), default="서울 강동구청 반려동물팀")
    date_to_meet = models.DateField()
    status = models.CharField(max_length=50, choices=(
        ("신청", "신청"),
        ("심사 중", "심사 중"),
        ("수락", "수락"),
        ("교육 중", "교육 중"),
        ("입양 완료", "입양 완료"),
        ("거절", "거절"),
    ), default="신청", db_index=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, unique=True)

