from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.user_list, name='user_list'),            # 전체 유저 목록 (로그인 전 공개)
    path('signup/', views.signup, name='signup'),           # 회원 가입
    path('login/', views.login_view, name='login'),         # 로그인
    path('logout/', views.logout_view, name='logout'),      # 로그아웃
]
