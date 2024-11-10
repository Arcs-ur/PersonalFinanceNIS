from django import forms
from .models import ExpenseEntry, IncomeEntry

# 支出条目的表单
class ExpenseEntryForm(forms.ModelForm):
    class Meta:
        model = ExpenseEntry
        fields = ['expense_category', 'amount', 'currency', 'expense_time', 'include_in_balance', 'include_in_budget', 'reimbursement', 'account', 'account_book']
        widgets = {
            'expense_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# 收入条目的表单
class IncomeEntryForm(forms.ModelForm):
    class Meta:
        model = IncomeEntry
        fields = ['income_category', 'amount', 'currency', 'income_time', 'include_in_balance', 'account', 'account_book']
        widgets = {
            'income_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
