from django.db import models
import uuid
from machinelearning.models import Profile

# Create your models here.

class Customer(models.Model):
    owner=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    featured_image=models.ImageField(null=True, blank=True, default="defaultt.jpg")
    customer_id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    customer_surname=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=200)
    customer_phone=models.IntegerField(null=False)
    customer_email=models.EmailField(max_length=200)
    date_registered=models.DateField(auto_now_add=True)
    account=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    

    def __str__(self):
        return self.customer_surname

class Accounts(models.Model):
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account_type=models.CharField(max_length=200)
    account_balance=models.IntegerField(null=False)
    account=models.ForeignKey(Customer, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.account

class Checking(models.Model):
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account=models.OneToOneField(Accounts, on_delete=models.CASCADE)
    account_balance=models.DecimalField( max_digits=25, decimal_places=2)
    available_balance=models.DecimalField( max_digits=25, decimal_places=2)
    credit_limit=models.DecimalField( max_digits=25, decimal_places=2)
 
    def __str__(self):
        return self.account

class Transactions(models.Model):
    transaction_id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    date=models.DateField(auto_now_add=True)
    available_balance=models.DecimalField( max_digits=25, decimal_places=2)
    amount_of_transcation=models.DecimalField( max_digits=25, decimal_places=2)
    transaction_description=models.CharField(max_length=500)
    account=models.ManyToManyField('Checking', blank=True)

    def __str__(self):
        return self.account

class Checking_Withdrawals(models.Model):
    checking_withdrawals_id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    account=models.ManyToManyField('Checking', blank=True)
    amount_withdrawn=models.DecimalField( max_digits=25, decimal_places=2)
    date_withdrawn=models.DateField(auto_now_add=True)
    time_withdrawn=models.TimeField(auto_now_add=True)
    account_balance=models.DecimalField(max_digits=25, decimal_places=2)
    

    def __str__(self):
        return self.account

class Checking_Deposits(models.Model):
    checking_deposits_id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    account=models.ManyToManyField('Checking', blank=True)
    amount_deposited=models.DecimalField( max_digits=25, decimal_places=2)
    date_deposited=models.DateField(auto_now_add=True)
    time_deposited=models.TimeField(auto_now_add=True)
    account_balance=models.DecimalField( max_digits=25, decimal_places=2)  
    

    def __str__(self):
        return self.account


class Savings(models.Model):
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account=models.OneToOneField(Accounts, on_delete=models.CASCADE, unique=True)
    account_balance=models.DecimalField( max_digits=25, decimal_places=2)
    
    def __str__(self):
        return self.account

class Savings_Withdrawals(models.Model):
    savings_withdrawn_id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account=models.ManyToManyField('Savings', blank=True)
    amount_withdrawn=models.DecimalField( max_digits=25, decimal_places=2)
    date_withdrawn=models.DateField(auto_now_add=True)
    time_withdrawn=models.TimeField(auto_now_add=True)
    account_balance=models.DecimalField( max_digits=25, decimal_places=2)

    def __str__(self):
        return self.account

class Savings_Deposits(models.Model):
    savings_deposits_id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account=models.ManyToManyField('Savings', blank=True)
    amount_deposited=models.DecimalField( max_digits=25, decimal_places=2)
    date_deposited=models.DateField(auto_now_add=True)
    time_deposited=models.TimeField(auto_now_add=True)
    account_balance=models.DecimalField( max_digits=25, decimal_places=2)  

    def __str__(self):
        return self.account

class Loans(models.Model):
    id=models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE, unique=False)
    amount_loaned=models.DecimalField( max_digits=25, decimal_places=2)
    date_loaned=models.DateField(auto_now_add=True)
    amount_standing=models.DecimalField( max_digits=25, decimal_places=2)
    due_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.account
    




    

