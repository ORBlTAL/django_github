from django.shortcuts import render
from .models import Article # 현재 디렉토리의 models.py에서 Article 클래스를 가져와야함
                                        # ㄴ views에서는 Article를 바로 인식 못하므로

# Create your views here.

# 전체 게시글 조회 후 메인 페이지 응답
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html' , context)
