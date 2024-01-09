from django import forms 
from .models import TransactionModel

class TransactionForm(forms.ModelForm):
    class Meta:
        model=TransactionModel
        fields=['amount','transaction_type']
        
    def __init__(self,*args, **kwargs):
        self.account=kwargs.pop('account')
        super().__init__(*args,**kwargs)
        
        self.fields['transaction_type'].disabled=True 
        self.fields['transaction_type'].widget=forms.HiddenInput()
    
    def save(self,commit=True):
        self.instance.account=self.account
        self.instance.balance_after_transaction=self.account.balance
        return super().save()
    

class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit_amount=100
        amount=self.cleaned_data.get('amount')
        
        if amount<min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )
        return amount 
    
class WithdrawForm(TransactionForm):
    def clean_amount(self):
        min_withdraw_amount=500
        max_withdraw_amount=20000
        amount=self.cleaned_data.get('amount')
        balance=self.account.balance
        
        if amount<min_withdraw_amount:
            raise forms.ValidationError(
                f'You must need to withdraw at least {min_withdraw_amount}$'
            )
        if amount>max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdrea atmost {max_withdraw_amount}$'
            )
        if amount>balance:
            raise forms.ValidationError(
                f'Insufficient Balance! You have {balance}$ in your Account.'
            )
        return amount
    
    
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount=self.cleaned_data.get('amount')
        return amount 