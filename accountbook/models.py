from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings

class AccountBook(models.Model):
    name = models.CharField(max_length=255)  # 账本名
    account_book_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)   # 账本ID
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name

class FundAccount(models.Model):
    name = models.CharField(max_length=255)  # 账户名
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # 余额
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True,primary_key=True)  # 自动生成 UUID 作为账户ID
    account_book = models.ForeignKey(AccountBook, related_name='fund_accounts', on_delete=models.CASCADE)  # 关联到账本
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    def __str__(self):
        return self.name
