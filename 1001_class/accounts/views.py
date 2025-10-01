from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm


def login(request):
    """
    사용자 로그인을 처리하는 뷰 함수
    GET: 로그인 폼을 보여줌
    POST: 로그인 인증을 처리함
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    """사용자 로그아웃 처리"""
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    """
    사용자 회원가입 뷰 함수
    GET: 회원가입 폼을 보여줌
    POST: 회원가입 처리
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 누구를 탈퇴하는지에 대한 유저 조회는 불필요
    # 유저 객체 삭제 
    request.user.delete()
    return redirect('articles:index')
