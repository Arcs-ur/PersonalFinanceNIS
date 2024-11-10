from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.cache import cache

class UserRegistrationTests(TestCase):
    def setUp(self):
        self.User = get_user_model()  # 获取用户模型
    
    def test_successful_registration(self):
        response = self.client.post(reverse('accounts:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'ValidPassword123',
            'password2': 'ValidPassword123',
            'verification_code': '123456'  # 假设这是你设置的验证码
        })
        
        # 检查响应是否为重定向
        self.assertEqual(response.status_code, 302)
        
        # 检查用户是否被创建
        user_exists = self.User.objects.filter(email='test@example.com').exists()
        self.assertTrue(user_exists)
    
    def test_register_with_existing_email(self):
        # 首先创建一个用户
        self.User.objects.create_user(username='existinguser', email='test@example.com', password='password123')

        # 试图使用相同的邮箱注册
        response = self.client.post(reverse('accounts:register'), {
            'username': 'newuser',
            'email': 'test@example.com',
            'password1': 'AnotherPassword123',
            'password2': 'AnotherPassword123',
            'verification_code': '123456'
        })

        # 检查响应中是否包含错误信息
        self.assertFormError(response, 'form', 'email', '此邮箱已被注册。')
