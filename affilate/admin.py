from django.contrib import admin
from .models import user_wallet, user_bonus
# Register your models here.


admin.site.register(user_wallet)
admin.site.register(user_bonus)
