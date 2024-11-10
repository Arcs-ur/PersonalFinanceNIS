from django.urls import path
from . import views
from .views import add_accountbook, add_fundaccount
app_name = 'dashboard'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # URL for adding an AccountBook
    #path('add_fundaccount/', views.add_fundaccount, name='add_fundaccount'),  # URL for adding a FundAccount
]
