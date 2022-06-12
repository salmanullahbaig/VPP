from django.db import models
from django.contrib.auth.models import User


class UserMessages(models.Model):
    name = models.CharField(max_length =22)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    subject = models.CharField(max_length=30)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.name}-{self.subject}"
    def get_message(self):
        #keys = {'api_key': self.api_key , 'secret_key': self.secret_key}
        return self.message
