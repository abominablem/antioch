from django.contrib import admin
from .models import (PaymentType, TransactionGroup, Account, Transaction,
                     TransactionDetail)

# Register your models here.

admin.site.register(PaymentType)
admin.site.register(TransactionGroup)
admin.site.register(Account)
# admin.site.register(Transaction)
admin.site.register(TransactionDetail)

class TransactionDetailInline(admin.TabularInline):
    model = TransactionDetail

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('fit_id', 'account_id', 'date_posted', 'counter_party',
                    'reference')

    list_filter = ('account_id', 'date_posted')

    inlines = [TransactionDetailInline]