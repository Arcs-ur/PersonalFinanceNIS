# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path("",include("accounts.urls")),
    path('admin/', admin.site.urls),
    # path("", include("authentication.urls")),  # add this
    path("accountbook/", include("accountbook.urls")),  # add this
    path("property/", include("property.urls")),  # add this
    path("dashboard/", include("dashboard.urls")),  # add this
    path("consumptionANDincome/",include("consumptionANDincome.urls")),
    path("accounts/",include("accounts.urls"))
    # path("", include("app.urls"))  # add this
    
]
