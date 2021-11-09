from django.shortcuts import render
from django.views import generic
from .models import (PaymentType, TransactionGroup, Account, Transaction,
                     TransactionDetail)

# Create your views here.

def transactions(request):
    transactions = Transaction.objects.filter()

    context = {'transactions': transactions}

    return render(request, 'transactions.html', context = context)


def transaction_details(request, fit_id):
    fit_id = fit_id.split("-")[0]
    details = TransactionDetail.objects.filter(
        detail_id__contains = fit_id)

    try:
        parent = details.first().get_parent()
    except AttributeError:
        parent = None

    context = {
        'transaction_details': details,
        'parent': parent
        }

    return render(request, 'transaction_details.html', context = context)