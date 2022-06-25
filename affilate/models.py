from django.db import models
from django.contrib.auth.models import User
from tronpy.keys import PrivateKey

# Create your models here.

class user_wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=200, unique=True)
    secret_key = models.CharField(max_length=200, unique=True)
    blance = models.FloatField(default=0)
    USDT = models.FloatField(default=0)
    TRX = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.user.username}-{self.blance}"
    def get_api(self):
        priv_key = PrivateKey(bytes.fromhex( self.secret_key ))
        keys = {'public_key': self.public_key , 'secret_key': priv_key}
        return keys

class user_bonus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bonus = models.CharField(max_length=200, unique=False)
    amount = models.FloatField(default=0)
    USDT = models.FloatField(default=0)
    TRX = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.user.username}-{self.bonus}-{self.amount}"


class User_transcations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount =  models.IntegerField(default=0)
    from_user =models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="to_user")
    credited = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.user.username} amount = {self.amount}"


class user_seed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seed = models.IntegerField(default=0)
    status = models.CharField(max_length=200, unique=False)
    seed_value =  models.IntegerField(default=0)
    paid = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.user.username} amount = {self.amount}"
