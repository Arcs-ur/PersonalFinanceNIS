# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import IncomeEntry,ExpenseEntry,MonthlyBudget
# Register your models here.
admin.site.register(IncomeEntry)
admin.site.register(ExpenseEntry)
admin.site.register(MonthlyBudget)