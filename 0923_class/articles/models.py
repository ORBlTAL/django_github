# 내장된 django 패키지 안에 db 서브패키지 안에 models.py라는 모듈을 import 한 것
from django.db import models 

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10) # 이름이 파스칼 케이스 -> 클래스에 속함
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) # 기본값이 반드시 필요, 빈값으로 사용못함 # 날짜
    updated_at = models.DateTimeField(auto_now=True ) # 시간
