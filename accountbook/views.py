# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .forms import AccountBookForm, FundAccountForm
from .models import AccountBook, FundAccount

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

def add_accountbook(request):
    if request.method == 'POST':
        form = AccountBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accountbook:accountbook_list')  # 重定向到账本列表页面
    else:
        form = AccountBookForm()
    return render(request, 'accountbook/add_accountbook.html', {'form': form})

def add_fundaccount(request):
    if request.method == 'POST':
        form = FundAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accountbook:fundaccount_list')  # 重定向到账户列表页面
    else:
        form = FundAccountForm()
    return render(request, 'accountbook/add_fundaccount.html', {'form': form})

def accountbook_list(request):
    query = request.GET.get('q', '')  # 获取 'q' 参数，默认为空字符串

    # 根据 'q' 参数过滤支出记录
    if query:
        accountbooks = AccountBook.objects.filter(name__icontains=query)  # 'icontains' 用于不区分大小写的模糊查询
    else:
        accountbooks = AccountBook.objects.all()
      # 获取所有账本
    return render(request, 'accountbook/accountbook_list.html', {'accountbooks': accountbooks})

# 显示所有账户
def fundaccount_list(request):
    query = request.GET.get('q', '')  # 获取 'q' 参数，默认为空字符串
    if query:
        fund_accounts = FundAccount.objects.filter(name__icontains=query)  # 'icontains' 用于不区分大小写的模糊查询
    else:
        fund_accounts = FundAccount.objects.all() 
     # 获取所有账户
    return render(request, 'accountbook/fundaccount_list.html', {'fund_accounts': fund_accounts})

# 删除账本
def delete_accountbook(request, accountbook_id):
    accountbook = get_object_or_404(AccountBook, account_book_id=accountbook_id)
    accountbook.delete()
    return redirect('accountbook:accountbook_list')  # 删除后重定向到账本列表页面

# 删除账户
def delete_fundaccount(request, account_id):
    fund_account = get_object_or_404(FundAccount, account_id=account_id)
    fund_account.delete()
    return redirect('accountbook:fundaccount_list')  # 删除后重定向到账户列表页面

def update_accountbook(request, accountbook_id):
    # 获取指定ID的账本
    accountbook = get_object_or_404(AccountBook, account_book_id=accountbook_id)
    
    if request.method == 'POST':
        form = AccountBookForm(request.POST, instance=accountbook)
        if form.is_valid():
            form.save()
            return redirect('accountbook:accountbook_list')  # 更新成功后重定向到账本列表页面
    else:
        form = AccountBookForm(instance=accountbook)
    
    return render(request, 'accountbook/update_accountbook.html', {'form': form, 'accountbook': accountbook})

# 更新账户
def update_fundaccount(request, account_id):
    # 获取指定ID的账户
    fund_account = get_object_or_404(FundAccount, account_id=account_id)
    
    if request.method == 'POST':
        form = FundAccountForm(request.POST, instance=fund_account)
        if form.is_valid():
            form.save()
            return redirect('accountbook:fundaccount_list')  # 更新成功后重定向到账户列表页面
    else:
        form = FundAccountForm(instance=fund_account)
    
    return render(request, 'accountbook/update_fundaccount.html', {'form': form, 'fund_account': fund_account})