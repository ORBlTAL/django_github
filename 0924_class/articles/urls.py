from django.urls import path
from . import views # 현재 디렉토리에서 views라는 모듈을 import 할거다

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'index' ) # 이미 pjt에서 주소 설정을했으므로 빈 문자열로 남긴다.
]

