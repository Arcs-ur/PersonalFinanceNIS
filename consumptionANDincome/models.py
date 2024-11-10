# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from accountbook.models import FundAccount, AccountBook  # 导入 FundAccount 和 AccountBook 模型

class ExpenseEntry(models.Model):
    # 支出种类选项
    EXPENSE_CATEGORIES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('entertainment', 'Entertainment'),
        ('shopping', 'Shopping'),
        ('utilities', 'Utilities'),
        ('others', 'Others'),
    ]
    
    # 货币种类选项
    CURRENCIES = [
        ('CNY', 'CNY'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('other', 'Other'),
    ]
    
    expense_id = models.AutoField(primary_key=True)  # 支出条目ID，自动生成
    expense_category = models.CharField(
        max_length=50,
        choices=EXPENSE_CATEGORIES,
        default='others'
    )  # 支出种类，使用 choices 限制选择
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 支出金额
    currency = models.CharField(
        max_length=10,
        choices=CURRENCIES,
        default='CNY'
    )  # 货币种类，使用 choices 限制选择
    expense_time = models.DateTimeField()  # 支出时间
    include_in_balance = models.BooleanField(default=False)  # 是否计入收支
    include_in_budget = models.BooleanField(default=False)  # 是否计入预算
    reimbursement = models.BooleanField(default=False)  # 是否报销
    account = models.ForeignKey(FundAccount, related_name='expense_entries', on_delete=models.CASCADE)  # 选择账户ID
    account_book = models.ForeignKey(AccountBook, related_name='expense_entries', on_delete=models.CASCADE)  # 记录账本ID

    def __str__(self):
        return f"Expense Entry {self.expense_id} - {self.get_expense_category_display()}"

class IncomeEntry(models.Model):
    # 收入种类选项
    INCOME_CATEGORIES = [
        ('salary', 'Salary'),
        ('investment', 'Investment'),
        ('business', 'Business'),
        ('gift', 'Gift'),
        ('others', 'Others'),
    ]
    
    # 货币种类选项
    CURRENCIES = [
        ('CNY', 'CNY'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('other', 'Other'),
    ]
    
    income_id = models.AutoField(primary_key=True)  # 收入条目ID，自动生成
    income_category = models.CharField(
        max_length=50,
        choices=INCOME_CATEGORIES,
        default='others'
    )  # 收入种类，使用 choices 限制选择
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # 收入金额
    currency = models.CharField(
        max_length=10,
        choices=CURRENCIES,
        default='CNY'
    )  # 货币种类，使用 choices 限制选择
    income_time = models.DateTimeField()  # 收入时间
    include_in_balance = models.BooleanField(default=False)  # 是否计入收支
    account = models.ForeignKey(FundAccount, related_name='income_entries', on_delete=models.CASCADE)  # 选择账户ID
    account_book = models.ForeignKey(AccountBook, related_name='income_entries', on_delete=models.CASCADE)  # 记录账本ID

    def __str__(self):
        return f"Income Entry {self.income_id} - {self.get_income_category_display()}"

class MonthlyBudget(models.Model):
    # 货币种类选项（可以与支出条目中的货币种类选项共用）
    CURRENCIES = [
        ('CNY', 'CNY'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('GBP', 'GBP'),
        ('other', 'Other'),
    ]

    year = models.IntegerField()  # 年份
    month = models.IntegerField()  # 月份 (1-12)
    total_budget = models.DecimalField(max_digits=10, decimal_places=2)  # 总预算
    currency = models.CharField(max_length=10, choices=CURRENCIES, default='CNY')  # 货币种类
    remaining_budget = models.DecimalField(max_digits=10, decimal_places=2)  # 剩余预算

    def __str__(self):
        return f"Budget for {self.year}-{self.month}"

    def save(self, *args, **kwargs):
        # 在保存之前，确保剩余预算等于总预算
        if not self.remaining_budget:
            self.remaining_budget = self.total_budget
        super(MonthlyBudget, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('year', 'month')