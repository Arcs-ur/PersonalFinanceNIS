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