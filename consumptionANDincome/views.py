from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from .models import ExpenseEntry, IncomeEntry
from .forms import ExpenseEntryForm, IncomeEntryForm
from .models import IncomeEntry, ExpenseEntry
from django.db.models import Sum

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


# 收入统计视图
from django.shortcuts import render
from .models import IncomeEntry
from django.db.models import Sum

# def income_statistic(request):
#     # 获取当前账户的所有收入记录
#     incomes = IncomeEntry.objects.all()  # 可以根据需要修改筛选条件
    
#     # 计算总收入
#     total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    
#     # 返回数据到模板
#     return render(request, 'consumptionANDincome/income_statistic.html', {
#         'incomes': incomes,
#         'total_income': total_income,
#     })
# # 支出统计视图



def income_statistic(request):
    # 获取当前账户的所有收入记录
    incomes = IncomeEntry.objects.all()  # 可以根据需要修改筛选条件
    
    # 计算总收入
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    
    # 返回数据到模板
    return render(request, 'consumptionANDincome/income_statistic.html', {
        'incomes': incomes,
        'total_income': total_income,
    })


def consumption_statistic(request):
    # 获取当前账户的所有支出记录
    consumptions = ExpenseEntry.objects.all()  # 可以根据需要修改筛选条件
    
    # 计算总支出
    total_consumption = consumptions.aggregate(total=Sum('amount'))['total'] or 0
    
    # 返回数据到模板
    return render(request, 'consumptionANDincome/consumption_statistic.html', {
        'consumptions': consumptions,
        'total_consumption': total_consumption,
    })

# 结余统计视图

def surplus_statistic(request):
    # 获取所有收入记录
    total_income = IncomeEntry.objects.aggregate(total=Sum('amount'))['total'] or 0
    
    # 获取所有支出记录
    total_consumption = ExpenseEntry.objects.aggregate(total=Sum('amount'))['total'] or 0
    
    # 计算结余
    surplus = total_income - total_consumption
    
    # 返回数据到模板
    return render(request, 'consumptionANDincome/surplus_statistic.html', {
        'total_income': total_income,
        'total_consumption': total_consumption,
        'surplus': surplus,
    })


# 添加支出
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumptionANDincome:expense_list')  # 添加成功后重定向到支出统计页面
    else:
        form = ExpenseEntryForm()

    return render(request, 'consumptionANDincome/add_expense.html', {'form': form})

# 删除支出
def delete_expense(request, expense_id):
    try:
        expense = ExpenseEntry.objects.get(expense_id=expense_id)
        expense.delete()
    except ExpenseEntry.DoesNotExist:
        pass  # 如果没有找到对应的支出项，可以选择记录日志或其他处理

    return redirect('consumptionANDincome:expense_list')  # 删除成功后重定向到支出统计页面

# 更新支出
def update_expense(request, expense_id):
    try:
        expense = ExpenseEntry.objects.get(expense_id=expense_id)
    except ExpenseEntry.DoesNotExist:
        return redirect('consumptionANDincome:expense_list')  # 如果没有找到对应的支出项，跳转到支出统计页面

    if request.method == 'POST':
        form = ExpenseEntryForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('consumptionANDincome:expense_list')  # 更新成功后重定向到支出统计页面
    else:
        form = ExpenseEntryForm(instance=expense)

    return render(request, 'consumptionANDincome/update_expense.html', {'form': form, 'expense': expense})

# 添加收入
def add_income(request):
    if request.method == 'POST':
        form = IncomeEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consumptionANDincome:income_list')  # 添加成功后重定向到收入统计页面
    else:
        form = IncomeEntryForm()

    return render(request, 'consumptionANDincome/add_income.html', {'form': form})

# 删除收入
def delete_income(request, income_id):
    try:
        income = IncomeEntry.objects.get(income_id=income_id)
        income.delete()
    except IncomeEntry.DoesNotExist:
        pass  # 如果没有找到对应的收入项，可以选择记录日志或其他处理

    return redirect('consumptionANDincome:income_list')  # 删除成功后重定向到收入统计页面

# 更新收入
def update_income(request, income_id):
    try:
        income = IncomeEntry.objects.get(income_id=income_id)
    except IncomeEntry.DoesNotExist:
        return redirect('consumptionANDincome:income_list')  # 如果没有找到对应的收入项，跳转到收入统计页面

    if request.method == 'POST':
        form = IncomeEntryForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('consumptionANDincome:income_list')  # 更新成功后重定向到收入统计页面
    else:
        form = IncomeEntryForm(instance=income)

    return render(request, 'consumptionANDincome/update_income.html', {'form': form, 'income': income})

def expenseincome_list(request):
    # 这里编写获取和展示收支总览的逻辑
    return render(request, 'consumptionANDincome/expenseincome_list.html')

# 收入视图
def income_list(request):
    # 这里编写获取和展示收入的逻辑
    query = request.GET.get('q', '')  # 获取 'q' 参数，默认为空字符串

    # 根据 'q' 参数过滤支出记录
    if query:
        incomes = IncomeEntry.objects.filter(income_category__icontains=query)  # 'icontains' 用于不区分大小写的模糊查询
    else:
        incomes = IncomeEntry.objects.all()
    
    return render(request, 'consumptionANDincome/income_list.html',{'incomes':incomes})


# 支出视图
def expense_list(request):
    # 这里编写获取和展示支出的逻辑
    query = request.GET.get('q', '')  # 获取 'q' 参数，默认为空字符串

    # 根据 'q' 参数过滤支出记录
    if query:
        expenses = ExpenseEntry.objects.filter(expense_category__icontains=query)  # 'icontains' 用于不区分大小写的模糊查询
    else:
        expenses = ExpenseEntry.objects.all()
    
    return render(request, 'consumptionANDincome/expense_list.html',{'expenses':expenses})