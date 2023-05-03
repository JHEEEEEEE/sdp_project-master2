from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('home/',views.home),
    # 일기장
    path('diary/',views.diary),
    # 로그인
    path('user/signin/',views.user_signin),
    # 로그아웃
    path('user/signout/', views.user_logout),
    # 회원가입
    path('user/signup/',views.user_signup),
    # 유튜브
    path('youtube/',views.youtube),
    # 뉴스
    path('news/',views.news),
    # 달력
    path('calendar/',views.calendar),
    # todolist
    path('todolist/',views.todolist),
    # book
    path('book/',views.book),
]
