from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # 添加自定义的字段到管理员页面中
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'profile_picture', 'level')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
