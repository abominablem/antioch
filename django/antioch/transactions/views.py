from django.shortcuts import render
from .models import (PaymentType, TransactionGroup, Account, Transaction,
                     TransactionDetail)

# Create your views here.

def index(request):
    num_transactions = Transaction.objects.all().count()
    num_details = TransactionDetail.objects.all().count()

    num_accounts = Account.objects.count()
    num_savings = Transaction.objects.filter(account_id__exact = '2').count()

    context = {
        'num_accounts': num_accounts,
        'num_details': num_details,
        'num_transactions': num_transactions,
        'num_savings': num_savings,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)