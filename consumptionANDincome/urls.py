from django.urls import path, re_path
from . import views
app_name = 'consumptionANDincome'

urlpatterns = [
    # 收入统计页面
    path('income_statistic/', views.income_statistic, name='income_statistic'),
    # 支出统计页面
    path('consumption_statistic/', views.consumption_statistic, name='consumption_statistic'),
    # 结余统计页面
    path('surplus_statistic/', views.surplus_statistic, name='surplus_statistic'),
    # 添加收入条目
    path('add_income/', views.add_income, name='add_income'),
    # 删除收入条目
    path('delete_income/<int:income_id>/', views.delete_income, name='delete_income'),
    # 更新收入条目
    path('update_income/<int:income_id>/', views.update_income, name='update_income'),
    
    # 添加支出条目
    path('add_expense/', views.add_expense, name='add_expense'),
    # 删除支出条目
    path('delete_expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
    # 更新支出条目
    path('update_expense/<int:expense_id>/', views.update_expense, name='update_expense'),
]