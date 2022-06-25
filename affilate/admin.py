from django.contrib import admin
from .models import user_wallet, user_bonus, User_transcations,user_seed
# Register your models here.


admin.site.register(user_wallet)
admin.site.register(user_bonus)
admin.site.register(User_transcations)

admin.site.register(user_seed)
