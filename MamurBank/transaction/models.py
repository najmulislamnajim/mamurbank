from django.db import models
from account.models import UserBankAccount
from .constants import TRANSACTION_TYPE

# Create your models here.
class TransactionModel(models.Model):
    account=models.ForeignKey(UserBankAccount,related_name='transaction',on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    balance_after_transaction=models.DecimalField(max_digits=12,decimal_places=2)
    transaction_type=models.IntegerField(choices=TRANSACTION_TYPE)
    timestamp=models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False) 
    class Meta:
        ordering=['timestamp']