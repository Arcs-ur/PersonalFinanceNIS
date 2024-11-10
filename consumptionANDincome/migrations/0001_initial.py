# Generated by Django 5.1.2 on 2024-11-10 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accountbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseEntry',
            fields=[
                ('expense_id', models.AutoField(primary_key=True, serialize=False)),
                ('expense_category', models.CharField(choices=[('food', 'Food'), ('transport', 'Transport'), ('entertainment', 'Entertainment'), ('shopping', 'Shopping'), ('utilities', 'Utilities'), ('others', 'Others')], default='others', max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('CNY', 'CNY'), ('USD', 'USD'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('other', 'Other')], default='CNY', max_length=10)),
                ('expense_time', models.DateTimeField()),
                ('include_in_balance', models.BooleanField(default=False)),
                ('include_in_budget', models.BooleanField(default=False)),
                ('reimbursement', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_entries', to='accountbook.fundaccount')),
                ('account_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expense_entries', to='accountbook.accountbook')),
            ],
        ),
        migrations.CreateModel(
            name='IncomeEntry',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('income_category', models.CharField(choices=[('salary', 'Salary'), ('investment', 'Investment'), ('business', 'Business'), ('gift', 'Gift'), ('others', 'Others')], default='others', max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('CNY', 'CNY'), ('USD', 'USD'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('other', 'Other')], default='CNY', max_length=10)),
                ('income_time', models.DateTimeField()),
                ('include_in_balance', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_entries', to='accountbook.fundaccount')),
                ('account_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income_entries', to='accountbook.accountbook')),
            ],
        ),
        migrations.CreateModel(
            name='MonthlyBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('total_budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('CNY', 'CNY'), ('USD', 'USD'), ('EUR', 'EUR'), ('JPY', 'JPY'), ('GBP', 'GBP'), ('other', 'Other')], default='CNY', max_length=10)),
                ('remaining_budget', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'unique_together': {('year', 'month')},
            },
        ),
    ]
