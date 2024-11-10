# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *
app_name = 'consumptionANDincome'
urlpatterns = [
    # # Matches any html file 
    # re_path(r'^.*\.html', views.pages, name='pages'),

    # # The home page
    # path('', views.index, name='home'),
]
