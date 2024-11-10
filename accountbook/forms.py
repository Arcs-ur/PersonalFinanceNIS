from django import forms
from .models import AccountBook, FundAccount

class AccountBookForm(forms.ModelForm):
    class Meta:
        model = AccountBook
        fields = ['name']  # 只包含需要用户填写的字段


class FundAccountForm(forms.ModelForm):
    class Meta:
        model = FundAccount
        fields = ['name', 'balance', 'account_book']  # 用户需要填写的字段