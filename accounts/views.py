from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.cache import cache
from .forms import CustomUserCreationForm
from django.core.mail import send_mail  # 确保导入
import random
import string
from django.http import JsonResponse
import json
from .models import CustomUser
from .forms import ResetPasswordForm

from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.conf import settings

from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm

from django.contrib.auth import logout

def send_verification_code(email):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    send_mail(
        '您的验证码',
        f'您的验证码是: {code}',
        'h1185038823@163.com',  # 发件人邮箱
        [email],
        fail_silently=False,
    )
    cache.set(email, code, timeout=300)
    print(f"Sending verification code: {code} to {email}")
    print(f"Stored Code for {email}: {code}")

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            verification_code = form.cleaned_data.get('verification_code')
            stored_code = cache.get(email)
            if verification_code == stored_code:
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful!')
                return redirect('accounts:login')
            else:
                messages.error(request, '验证码错误，请重新输入。')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

def send_code_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            if email:
                if CustomUser.objects.filter(email=email).exists():
                    return JsonResponse({'success': False, 'error': '此邮箱已被注册。'}, status=400)
                send_verification_code(email)
                return JsonResponse({'success': True, 'message': '验证码已发送，请检查您的邮箱。'}, status=200)
            else:
                return JsonResponse({'success': False, 'error': '请输入有效的邮箱地址。'}, status=400)
        except json.JSONDecodeError as e:
           return JsonResponse({'success': False, 'error': '请求解析失败', 'details': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': '无效请求，仅支持POST请求。'}, status=400)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard:dashboard') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if CustomUser.objects.filter(email=email).exists():
                send_verification_code(email)
                request.session['verified_email'] = email  # 确保邮箱被存储
                messages.success(request, '验证码已发送，请检查您的邮箱。')
                return redirect('accounts:verify_code')  # 重定向到验证码验证页面
            else:
                messages.error(request, '该邮箱未注册。')
        else:
            messages.error(request, '请输入有效的邮箱地址。')
    return render(request, 'accounts/forgot_password.html')

def verify_code_view(request):
    print(f"Session Data: {request.session.items()}")  # 打印会话数据
    print(f"Received Email: {request.POST.get('email')}, Code: {request.POST.get('code')}")
    if request.method == 'POST':
        email = request.POST.get('email')
        code = request.POST.get('code')
        stored_code = cache.get(email)

        print(f"Session Email: {request.session.get('verified_email')}, Received Email: {email}, Code: {code}, Stored Code: {stored_code}")

        if code == stored_code:
            request.session['verified_email'] = email  # 存储已验证的邮箱
            return redirect('accounts:reset_password')  # 验证成功后重定向到重置密码页面
        else:
            messages.error(request, '验证码错误，请重新输入。')
    return render(request, 'accounts/verify_code.html')

def reset_password_view(request):
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            email = request.session.get('verified_email')
            user = CustomUser.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            messages.success(request, '密码重置成功，请登录。')
            return redirect('accounts:login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = ResetPasswordForm()
    
    return render(request, 'accounts/reset_password.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user  # 获取当前登录的用户
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, '个人资料已更新！')
            return redirect('accounts:profile')  # 更新成功后重定向到个人资料页面
    else:
        form = ProfileUpdateForm(instance=user)

    # 处理头像的显示
    profile_picture_url = user.profile_picture.url if user.profile_picture else '/static/assets/img/avatars/8.jpg'

    return render(request, 'accounts/profile.html', {
        'form': form,
        'profile_picture_url': profile_picture_url,
    })

    return render(request, 'accounts/profile.html', {'form': form})

@login_required
def settings_view(request):
    return render(request, 'accounts/settings.html')

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 保持用户登录状态
            messages.success(request, '密码修改成功！')  # 提示用户
            return redirect('accounts:settings')  # 修改成功后重定向
        else:
            # 提示用户表单有误
            messages.error(request, '修改密码时出现问题，请检查您的输入。')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('accounts:login')  # 重定向到登录页面