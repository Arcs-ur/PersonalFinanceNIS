# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import uuid


class AccountBook(models.Model):
    name = models.CharField(max_length=255)  # 账本名
    account_book_id = models.IntegerField(unique=True)  # 账本ID

    def __str__(self):
        return self.name

class FundAccount(models.Model):
    name = models.CharField(max_length=255)  # 账户名
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # 余额
    account_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # 自动生成 UUID 作为账户ID
    account_book = models.ForeignKey(AccountBook, related_name='fund_accounts', on_delete=models.CASCADE)  # 关联到账本

    def __str__(self):
        return self.name
