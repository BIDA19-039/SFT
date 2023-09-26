from django.contrib import admin

# Register your models here.
from .models import Customer, Accounts, Checking, Savings, Transactions, Loans, Savings_Withdrawals, Savings_Deposits, Checking_Withdrawals, Checking_Deposits

admin.site.register(Customer)
admin.site.register(Accounts)
admin.site.register(Checking)
admin.site.register(Savings)
admin.site.register(Savings_Withdrawals)
admin.site.register(Savings_Deposits)
admin.site.register(Checking_Withdrawals)
admin.site.register(Checking_Deposits)
admin.site.register(Transactions)
admin.site.register(Loans)

