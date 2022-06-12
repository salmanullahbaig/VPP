from django.db import models
from django.contrib.auth.models import User

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
        keys = {'public_key': self.public_key , 'secret_key': self.secret_key}
        return keys

class user_bonus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bonus = models.CharField(max_length=200, unique=True)
    amount = models.FloatField(default=0)
    USDT = models.FloatField(default=0)
    TRX = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.user.username}-{self.bonus}-{self.blance}"
