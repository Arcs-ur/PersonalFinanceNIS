# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import AccountBook,FundAccount
# Register your models here.
admin.site.register(AccountBook)
admin.site.register(FundAccount)