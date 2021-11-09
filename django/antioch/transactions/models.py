from django.db import models
from django.urls import reverse

# Create your models here.

class PaymentType(models.Model):
    """
    [")))", "ATM", "BP", "CR", "DD", "SO", "TFR", "VIS", "DR"]
    """
    name = models.CharField(max_length = 15,
                            verbose_name = "Payment type",
                            primary_key = True)

    def __str__(self):
        return self.name

class TransactionGroup(models.Model):
    """
    ["Expense (Food)", "Expense (Entertainment)",
     "Expense (Travel)", "Expense (Clothes)",
     "Expense (Books)", "Expense (Rent/Bills)",
     "Expense (Other)", "Savings", "Cash", "Income (Work)",
     "Income (Other)", "Interest"]
    """
    name = models.CharField(max_length = 255,
                            verbose_name = "Transaction group",
                            primary_key = True)

    def __str__(self):
        return self.name

class Account(models.Model):
    account_id = models.CharField(max_length = 255,
                                  verbose_name = "Account ID",
                                  primary_key = True)

    account_name = models.CharField(max_length = 255,
                                    verbose_name = "Account Name",
                                    blank = False, null = False)

    ofx_name = models.CharField(max_length = 255,
                                verbose_name = "OFX Name",
                                blank = True, null = True)

    class Meta:
        ordering = ['account_id']

    def __str__(self):
        return "%s - %s" % (self.account_id, self.account_name)

    def get_absolute_url(self):
        """
        Returns the url to view the balance and transaction history of a given
        account, split by month of posting date
        """
        #TODO
        return

class Transaction(models.Model):
    fit_id = models.CharField(max_length = 255,
                              verbose_name = "FIT ID",
                              primary_key = True,
                              blank = False)

    account_id = models.ForeignKey('Account', on_delete = models.PROTECT)

    date_posted = models.DateField(verbose_name = "Posting Date",
                                   blank = False)

    date_entered = models.DateField(verbose_name = "Entry Date")
    date_inserted = models.DateField(verbose_name = "Date Inserted",
                                     blank = False)

    counter_party = models.CharField(max_length = 255,
                                     verbose_name = "Counter Party",
                                     blank = False)

    reference = models.CharField(max_length = 255,
                                 verbose_name = "Reference",
                                 blank = True, null = True)

    transaction_type = models.CharField(max_length = 255,
                                        verbose_name = "Transaction type",
                                        blank = False)

    payment_type = models.ForeignKey('PaymentType',
                                     on_delete = models.PROTECT)

    amount = models.FloatField(verbose_name = "Amount",
                               blank = False)

    class Meta:
        ordering = ['date_posted', 'fit_id']

    def get_absolute_url(self):
        """Returns the url to view all detail in a specific transaction"""
        #TODO
        return

    def __str__(self):
        return "%s %s %s %s" % (self.fit_id, self.date_posted,
                                self.amount, self.counter_party)

class TransactionDetail(models.Model):
    fit_id = models.ForeignKey('Transaction', on_delete = models.PROTECT)

    detail_id = models.CharField(max_length = 255,
                                 verbose_name = "Transaction Detail ID",
                                 primary_key = True,
                                 blank = False)

    transaction_group = models.ForeignKey('TransactionGroup',
                                          on_delete = models.PROTECT)

    amount = models.FloatField(verbose_name = "Amount",
                              blank = False)

    comment = models.CharField(max_length = 4095,
                               verbose_name = "Comment",
                               blank = True, null = True)

    class Meta:
        ordering = ['fit_id']

    def __str__(self):
        return "%s %s" % (self.detail_id, self.amount)

    def get_absolute_url(self):
        """
        Returns the url to view a specific detail of a certain transaction
        """
        #TODO
        return