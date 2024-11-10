from django.urls import path
from . import views
app_name = 'accountbook'
urlpatterns = [
    path('add_accountbook/', views.add_accountbook, name='add_accountbook'),  # URL for adding an AccountBook
    path('add_fundaccount/', views.add_fundaccount, name='add_fundaccount'),  # URL for adding a FundAccount
    path('update_accountbook/<uuid:accountbook_id>/', views.update_accountbook, name='update_accountbook'),
    path('update_fundaccount/<uuid:account_id>/', views.update_fundaccount, name='update_fundaccount'),
    path('accountbook_list/', views.accountbook_list, name='accountbook_list'),
    path('fundaccount_list/', views.fundaccount_list, name='fundaccount_list'),
]
