from django.urls import path
from . import views
from .views import add_accountbook, add_fundaccount
app_name = 'accountbook'
urlpatterns = [
    path('add_accountbook/', views.add_accountbook, name='add_accountbook'),  # URL for adding an AccountBook
    path('add_fundaccount/', views.add_fundaccount, name='add_fundaccount'),  # URL for adding a FundAccount
]
