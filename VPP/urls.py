
from django.contrib import admin
from django.urls import path , include
from . import views
from accounts import urls as accounts_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name= 'index'),
    path('wallet/',views.walletView,name= 'wallet'),
    path('message/',views.sendMessageView,name= 'message'),
    path('refers/',views.refersView, name= 'refers'),
    path('account/',include(accounts_urls)),
]
