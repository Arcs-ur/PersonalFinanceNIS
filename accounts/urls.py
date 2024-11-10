from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'accounts'
urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('send_code/', views.send_code_view, name='send_code'),  # 新增发送验证码的路由
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),  # 忘记密码页面
    path('verify_code/', views.verify_code_view, name='verify_code'),  # 验证码验证页面
    path('reset_password/', views.reset_password_view, name='reset_password'),  # 重置密码页面
    path('profile/', views.profile_view, name='profile'),#个人资料页面
    path('settings/', views.settings_view, name='settings'),
    path('settings/change_password/', views.change_password, name='change_password'),
    path('logout/', views.logout_view, name='logout'),

]
