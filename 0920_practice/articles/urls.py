from django.contrib import admin
from django.urls import path
from . import views
# 명시적 상대경도를 사용, 같은 폴더내에 있으므로 '.' 으로 표시(그냥 import만 해도 되긴 함)
app_name = 'articles'
urlpatterns = [ 
    path('', views.index , name= 'index'), # 어차피 articles를 pjt urls.py가 가리키므로 생략
    path('dinner/', views.dinner , name = 'dinner'), # 주소가 길어지면 적기 힘드니 이름을 지어서 주소 대신 사용 
    path('search/', views.search , name = 'search'),
    path('throw/', views.throw , name = 'throw'),
    path('catch/', views.catch , name = 'catch'),
    path('<int:num>/', views.detail , name = 'detail'),
]
